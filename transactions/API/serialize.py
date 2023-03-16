from rest_framework import serializers
from datetime import date
from transactions.models import Transaction


# def transaction_type_validator(value):
#     print("In duration_validator")
#     if value < 1 or value > 3:
#         raise serializers.ValidationError("Your transaction type should between 1 to 3")

class TransactionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    account_id = serializers.CharField(max_length=256)
    amount = serializers.CharField()
    timestamp = serializers.DateField(write_only=True, default=date.today())
    balance_after_transaction = serializers.CharField()
    transaction_type = serializers.CharField() #validators=[transaction_type_validator]

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_field = ['id']

    def validate_transaction_type(self, value):
        if not value.upper() in ['1', '2', '3']:
            raise serializers.ValidationError("Valid values are. '1'-deposit, '2'-Withdrawal, '3'- Interest")
        return value


