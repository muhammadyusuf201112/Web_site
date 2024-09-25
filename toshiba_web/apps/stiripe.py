from urllib import request
from django.conf import settings
from django.http import JsonResponse
import stripe # type: ignore

def charge(request):
    if request.method == 'POST':
        try:
            price = int(float(request.POST['price']) * 100)  # Convert price to cents
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                amount=price,
                currency='uzs',
                description='Toʻlov ma\'lumotlari',
                source=token,
            )
            return JsonResponse({'message': 'Toʻlov muvaffaqiyatli!'})
        except stripe.error.CardError as e:
            return JsonResponse({'message': f'Xato: {str(e)}'})



@apps.route('/charge', methods=['POST']) # type: ignore
def charge():
    try:
        # Get product price from the form
        price = int(float(request.form['price']) * 100)  # convert to cents
        token = requzest.form['stripeToken'] # type: ignore

        # Create a charge using Stripe's library
        charge = stripe.Charge.create(
            amount=price,  # Price from form in cents
            currency="uzs",
            description="Toʻlov ma'lumotlari",
            source=token
        )
        return jsonify({"message": "Toʻlov muvaffaqiyatli!"}) # type: ignore
    except stripe.error.StripeError as e:
        return jsonify({"message": f"Xato: {e}"}) # type: ignore
