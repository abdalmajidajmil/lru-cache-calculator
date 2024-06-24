import enum
from lru_cache import LruCache


class Operator(enum.Enum):
    """
    class of type enum represent operators.
    """
    mul = '*'
    sum = '+'
    sub = '-'
    div = '/'


class Calculation:
    """
    class Calculation to Calculate arithmetic operations to store in cache afterward.
    """

    @staticmethod
    def calculation(left: (int, float), op: Operator, right: (int, float)) -> (int, float):
        """

        :param left: left operand.
        :param op: operator.
        :param right: right operand.
        :return: result.
        """
        if op == Operator.mul:
            return left * right
        elif op == Operator.sum:
            return left + right
        elif op == Operator.sub:
            return left - right
        elif op == Operator.div:
            return left / right


class CacheCalculator:

    def __init__(self, size: int):
        """
        :param size: size for Lru cache.
         attribute __lrucache:  to store arithmetic operations (keys: operations, values: results).
        """
        self.__lrucache = LruCache(size)

    def calculate(self, left_side: int, right_side: int, operator: str) -> tuple:
        """

        :param left_side: left operand.
        :param right_side: right operand.
        :param operator: operator.
        :return: result of an operation and True if we used cache, or False if We calculated and didn't use cache.
        """

        operator = Operator[operator]  # to consider operator as one of the 4 types that defined in enum class.
        operation = f"{left_side} {operator.value} {right_side}"  # <left openad> <operator(+,-,/,*)> <right operand>.
        rol = f"{right_side} {operator.value} {left_side}"  # <right openad> <operator(+,-,/,*)> <left operand>.

        if operation in self.__lrucache.cache:  # if operation stored as key in cache, then call her value(result).
            return self.__lrucache.get(operation), True  # and return True, because we used cache.
        # + and * are commutative, so we need to concern about <rol> if it's saved in cache.
        elif operator.value in [Operator.mul.value, Operator.sum.value] and rol in self.__lrucache.cache:
            return self.__lrucache.get(rol), True

        else:  # if operation is not saved in cache, then call Calculation.calculation to calculate and save operation
            # and result as pair in cache
            result = Calculation.calculation(left_side, operator, right_side)
            self.__lrucache.put(operation, result)
            return result, False
