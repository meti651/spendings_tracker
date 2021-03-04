# Spending tracker

A RESTful API to track our spending.

---

## Endpoints

### Add new spending

Send a `POST` request to the endpoint `api/spendings` with a JSON object in the body.
The object is structured in the next way:
```javascript
{
    amount: integer,
    currency: string,
    description: string [optional]
    date: timestamp [optional]
}
```
>**amount**
>An integer describing the amount we spent
>
>**currency**
>The name of the currency (ex.: *dollar* / *euro*).
>
>**[description]**
>
>A text representing anything we want to add to the spending. The text can be maximum 200 character long. If left empty the description will be set to an empty string.
>
>**[date]**
>
>The date when the spending was made. If the date is left empty, the server set it to the actual time in the `UTC` timezone.

If some properties are not in the requested type, the request returns with a status code of 400 with the message `Wrong properties set`.

---

### List all the spendings

Send a `GET` request to the endpoint `api/spendings`.

The request returns a JSON list of spending objects.
The objects contains the properties:

```javascript
{
    model: string
    pk: integer,
    amount: integer,
    currency: string,
    description: string,
    date: timestamp
}
```
>**model**
>
>A string representing the object model type. This is mostly *spendingstracker.spending*.
>
>**id**
>
>An integer representing the spending id/primary key.
>
>**amount**
>
>An integer representing the amount spent.
>
>**currency**
>
>A string representing the spent amount currency (ex.: *dollar*)
>
>**description**
>
>A string representing added information to the spending.
>
>**date**
>
>The date in timestamp format representing the spending set date.

---

### List all the spendings ordered by the amount

Send a `GET` request to the endpoint `api/spendings/order/<order_by>` where the `<order_by>` can be the `date` or the `amount` word.

---

### List all the spendings filtered by the currency

Send a `GET` request to the endpoint `api/spendings/filter/<currency>` where the `<currency>` is a text with the currency type.

---

### Delete spending

Send a `DELETE` request to the endpoint `api/spendings/<id>/delete` where the `<id>` is the `id` of the spending we want to delete.

---

### Update spending

Send a `PUT` request to the endpoint `api/spending/<id>/update` where the `<id>` is the `id` of the spending we want to update.
Also send an object in the request body with the updated information.

```javascript
{
    amount: integer,
    currency: string,
    description: string,
    date: timestamp
}
```
