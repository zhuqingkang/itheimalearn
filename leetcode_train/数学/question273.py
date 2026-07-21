class Solution:
    # 预定义常量字典，避免每次调用 helper 时重复创建
    _data_num = {
        '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
        '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    _data_num_ten = {
        '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen',
        '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen',
        '18': 'Eighteen', '19': 'Nineteen'
    }
    _data_num_tens = {
        '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty',
        '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'
    }
    _data_num_unit = {1: 'Thousand', 2: 'Million', 3: 'Billion'}

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        # 核心递归辅助函数：处理小于 1000 的正整数
        def helper(n: int) -> str:
            parts = []

            # 处理百位
            if n >= 100:
                parts.append(self._data_num[str(n // 100)])
                parts.append("Hundred")
                n %= 100

            # 处理十位和个位
            if 10 <= n < 20:
                parts.append(self._data_num_ten[str(n)])
            else:
                # 处理整十数
                if n >= 20:
                    parts.append(self._data_num_tens[str(n // 10)])
                    n %= 10
                # 处理个位数
                if n > 0:
                    parts.append(self._data_num[str(n)])

            # 使用 join 一次性拼接，避免中间字符串产生和多余空格
            return " ".join(parts)

        result_parts = []
        unit_index = 0

        # 按千位分段处理
        while num > 0:
            current_part = num % 1000
            if current_part != 0:
                segment = helper(current_part)
                if unit_index > 0:
                    segment += " " + self._data_num_unit[unit_index]
                result_parts.append(segment)

            num //= 1000
            unit_index += 1

        # 由于是从低位到高位处理，最终结果需要反转
        return " ".join(reversed(result_parts))