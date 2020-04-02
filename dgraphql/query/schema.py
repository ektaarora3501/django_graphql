import graphene
from graphene_django.types import DjangoObjectType,ObjectType
from query.models import Writer,Books


# property type for graphene
class WriterType(DjangoObjectType):
    class Meta:
        model=Writer
#
class BooksType(object):
    class Meta:
        model = Books



class Query(ObjectType):
    writer = graphene.Field(WriterType,id=graphene.Int())
    # book = graphene.Field(BooksType,id=graphene.Int())
    writers = graphene.List(WriterType)
    # books = graphene.List(BooksType)


# **kwargs used to pass dictionary parameter to the function

    def resolve_writer(self,info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Writer.objects.get(pk=id)

        return None
#
    # def resolve_book(self,info,**kwargs):
    #     id = kwargs.get('id')
    #
    #     if id is not None:
    #         return Book.objects.get(pk=id)
    #
    #     return None

    def resolve_writers(self,info,**kwargs):
        return Writer.objects.all()
    #
    # def resolve_books(self,info,**kwargs):
    #     return Book.objects.all()

#
# #creating mutations .. i.e. creating input type and payload to change data on the server
#
class WriterInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

# class BookInput(graphene.InputObjectType):
#     id = graphene.ID()
#     title = graphene.String()
#     writers = graphene.String() #must be list here

#
# creating mutations for writers

class CreateWriter(graphene.Mutation):
    class Arguments:
        input = WriterInput(required=True)

    ok = graphene.Boolean()
    writer = graphene.Field(WriterType)

    @staticmethod
    def mutate(root,info,input=None):
        ok = True
        writer_instance = Writer(name=input.name)
        writer_instance.save()

        return CreateWriter(ok=ok,writer=writer_instance)


class UpdateWriter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = WriterInput(required=True)

    ok = graphene.Boolean()
    writer=graphene.Field(WriterType)

    @staticmethod
    def mutate(root,info,id,input=None):
        ok = False
        writer_instance = Writer.objects.get(pk=id)

        if writer_instance:
            ok = True
            writer_instance.name = input.name
            writer_instance.save()

            return UpdateWriter(ok=ok,writer=writer_instance)

        return UpdateWriter(ok=ok,writer=None)


#
# # creating mutautions for books

# class CreateBook(graphene.Mutation):
#     class Arguments:
#         input = BookInput(required=True)
#
#     ok = graphene.Boolean()
#     book = graphene.Field(BooksType)
#
#     @staticmethod
#     def mutate(root,info,input=None):
#         ok = True
#         writers=[]
#
#         for writer_input in input.writers:
#             writer = Writer.objects.get(pk=writer_input.id)
#
#             if writer is None:
#                 return CreateBook(ok = False,book = None)
#
#             writers.append(writer)
#
#             book_instance = Book(
#             title = input.title,
#             )
#
#             book_instance.save()
#             book_instance.writers.set(writers)
#
#             return CreateBook(ok=ok,book=book_instance)
#
#
#
#
# class UpdateBook(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = BookInput(required=True)
#
#     ok = graphene.Boolean()
#     book = graphene.Field(BooksType)
#
#     @staticmethod
#     def mutate(root,info,input=None):
#         ok = False
#         book_instance = Book.objecs.get(pk=id)
#
#         if book_instance:
#             ok = True
#             writers = []
#
#             for writer_input in input.writers:
#                 writer = Writer.objects.get(pk=writer_input.id)
#
#                 if writer is None:
#                     return UpdateBook(ok=False,book=None)
#
#                 writers.append(writer)
#                 book_instance.title=input.title
#                 book_instance.writers.set(writers)
#
#                 return UpdateBook(ok=ok,book=book_instance)
#
#             return UpdateBook(ok=ok,book=None)
#

class Mutation(graphene.ObjectType):
    create_writer = CreateWriter.Field()
    # create_book = CreateBook.Field()
    update_writer = UpdateWriter.Field()
    # update_book = UpdateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
