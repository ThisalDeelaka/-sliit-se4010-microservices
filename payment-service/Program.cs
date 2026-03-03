using System.Collections.Generic;
using System.Linq;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var payments = new List<Payment>();
var idCounter = 1;

app.MapGet("/payments", () => Results.Ok(payments));

app.MapPost("/payments/process", (PaymentProcessRequest request) =>
{
    if (request.OrderId <= 0 || request.Amount < 0 || string.IsNullOrWhiteSpace(request.Method))
    {
        return Results.BadRequest(new { message = "Invalid payload. orderId, amount, and method are required." });
    }

    var payment = new Payment(
        Id: idCounter++,
        OrderId: request.OrderId,
        Amount: request.Amount,
        Method: request.Method,
        Status: "SUCCESS"
    );

    payments.Add(payment);
    return Results.Json(payment, statusCode: StatusCodes.Status201Created);
});

app.MapGet("/payments/{id:int}", (int id) =>
{
    var payment = payments.FirstOrDefault(p => p.Id == id);
    return payment is null
        ? Results.NotFound(new { message = "Payment not found" })
        : Results.Ok(payment);
});

app.Run();

public record Payment(int Id, int OrderId, decimal Amount, string Method, string Status);

public record PaymentProcessRequest(int OrderId, decimal Amount, string Method);
