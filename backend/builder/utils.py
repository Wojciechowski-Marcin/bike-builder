from random import randint


def get_random_object(queryset):
    count = queryset.count()
    return queryset[randint(0, count-1)] if count else (
        queryset.first() if count == 1 else None)


def querysets_intersection(queryset_list):
    qs_length = len(queryset_list)
    merged_querysets = None

    if qs_length >= 1:
        merged_querysets = queryset_list[0]
        if qs_length != 1:
            merged_querysets.intersection(*queryset_list)

    return merged_querysets


def is_any_key_in_dict(keys, dict):
    return any([(key in dict for key in keys)])


def igetattr(obj, attr):
    for a in dir(obj):
        if a.lower() == attr.lower():
            return getattr(obj, a)
