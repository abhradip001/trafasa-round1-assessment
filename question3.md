# Question 3 – REST APIs & Git

## 1. REST API Design

### Endpoint

```http
POST /api/payments/initiate
```

### Request Body

```json
{
  "order_id": "ORD-1001",
  "customer_id": "CUS-2001",
  "amount": 2500.00,
  "currency": "INR",
  "payment_method": "UPI"
}
```

### Success Response

```json
{
  "status": "success",
  "payment_id": "PAY-56789",
  "payment_url": "https://payment.example.com/PAY-56789",
  "message": "Payment initiated successfully."
}
```

---

## 2. Git Commands

Update the feature branch with the latest changes from `develop` using **rebase**.

```bash
git checkout feature/add-whatsapp-integration

git fetch origin

git rebase origin/develop
```

If conflicts occur:

```bash
git add .

git rebase --continue
```

Push the updated branch:

```bash
git push --force-with-lease
```

### Why Rebase?

- Keeps the Git history clean and linear.
- Avoids unnecessary merge commits.
- Makes collaboration easier.
- Reduces merge conflicts before integrating the feature branch.