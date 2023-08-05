from src.controllers.product_controller import *

routes = {
    "product": {
        "index": {
            "route": "/products",
            "controller": ProductIndexController.as_view('product_index')
        },
        "destroy": {
            "route": "/products/<int:id>/destroy",
            "controller": ProductDestroyController.as_view('product_destroy')
        },
        "edit": {
            "route": "/products/<int:id>/edit",
            "controller": ProductEditController.as_view('product_edit')
        },
        "update": {
            "route": "/products/<int:id>/update",
            "controller": ProductEditController.as_view('product_update')
        },
    }
}