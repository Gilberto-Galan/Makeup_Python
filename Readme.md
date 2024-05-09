# Makeup API

En este proyecto se estara trabajando con el lenguaje de Python 3 y la API de Makeup API herokuapp.

Consiste en buscar el maquillaje por marca, etiqueta, categoria y por precio minimo o mayor.


## Documentacion

El uso de la API nos permite visualizarlo en la terminal en el formato JSON

[Makeup API](https://makeup-api.herokuapp.com/api/v1/products.json)


## API Refencias

#### Get all items

```http
  GET / API / JSON
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `product_type` | `string` | El tipo de maquillaje que se busca (es decir, lápiz labial, delineador de ojos). |
| `product_category`| `string` | Subcategoría para cada tipo de maquillaje. (es decir, el brillo de labios es una categoría de lápiz labial). |
| `product_tags` | `string, list separated by commas` | Opciones con las que se podría etiquetar cada producto. |
| `product_tags` | `string, list separated by commas` | Opciones con las que se podría etiquetar cada producto.|
| `brand` | `string` | Devolverá todos los productos de cada marca. |
| `price_greater_than` | `number` | Devolverá una lista de productos con precio mayor al número indicado (exclusivo) |
| `price_less_than` | `number` | Devolverá una lista de productos con precio menor que el número indicado (exclusivo) |