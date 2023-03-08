from django_model_mixins import mixins

class MixinsLogData(mixins.CreationDateMixin, mixins.EditDateMixin):
    # Adds a created_at field which is automatically set to current time (using timezone.now()) on model creation.
    # Adds a edited_at field which is automatically set to current time (using timezone.now()) on every model save.
    class Meta:
        abstract = True
        