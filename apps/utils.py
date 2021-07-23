from django.db.models import Model


def update_model(*, model: Model, **data):
    for field_name, field_value in data.items():
        if hasattr(model, field_name):
            setattr(model, field_name, field_value)
    model.save()
    return model
