import typing as t
from collections import defaultdict

from rest_framework import serializers


class GroupManyRelatedField(serializers.Field):
    def __init__(self, group_field: str, return_field: str, sub_return_field: str | None = None, **kwargs):
        self.group_field: str = group_field
        self.return_field: str = return_field
        self.sub_return_field: str | None = sub_return_field
        super().__init__(**kwargs)

    def to_representation(self, instance):
        data: t.DefaultDict[str, list] = defaultdict(list)

        for obj in instance.all():
            key = getattr(obj, self.group_field)
            if callable(key):
                key = key()

            value = getattr(obj, self.return_field)
            if value.__class__.__name__ == 'ManyRelatedManager':
                value = [getattr(sub_obj, self.sub_return_field) for sub_obj in value.all()]    # type: ignore

            data[key].append(value)
        return data
