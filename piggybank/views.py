from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Transaction, PiggyBank
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone

@api_view(['POST'])
def add_money(request):
    amount = request.data.get('amount')

    if amount is not None:
        # Use the first PiggyBank or create one if none exists
        piggy_bank, created = PiggyBank.objects.get_or_create(id=1)

        try:
            Transaction.objects.create(amount=amount, piggy_bank=piggy_bank)
            return JsonResponse({'message': 'Money added successfully'}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            print(f'IntegrityError: {e}')
            return JsonResponse({'error': f'IntegrityError: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(f'Unexpected Error: {e}')
            return JsonResponse({'error': f'Internal Server Error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Invalid data. Make sure to provide amount.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def break_piggy_bank(request):
    # Get total amount before clearing transactions
    total_amount = Transaction.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Clear all transactions
    Transaction.objects.all().delete()

    # Set the piggy bank status to broken
    piggy_bank = PiggyBank.objects.get_or_create(id=1)[0]
    piggy_bank.is_broken = True
    piggy_bank.save()

    return JsonResponse({'total_amount': total_amount, 'message': 'Piggy bank broken and transactions cleared'})

@api_view(['GET'])
def view_transactions(request):
    transactions = Transaction.objects.all()    
    transactions_data = [{"amount": str(t.amount), "timestamp": t.timestamp.isoformat() + 'Z'} for t in transactions]
    
    return Response(transactions_data)
