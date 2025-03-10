from pydantic import BaseModel, ConfigDict, constr, conint


class RecipeBase(BaseModel):
    name: constr(max_length=50)
    cooking_time: conint(gt=0)
    ingredients: constr(max_length=500)
    description: constr(max_length=250)


class RecipeIn(RecipeBase): ...


class RecipeOut(RecipeBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class DishBase(BaseModel):
    name: constr(max_length=50)
    views: conint(ge=0)
    cooking_time: conint(gt=0)


class DishIn(DishBase): ...


class DishOut(DishBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
