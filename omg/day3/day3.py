{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "128a204c-16de-4c40-8167-3e1e0f1be53a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_prime(n):\n",
    "    if n <= 1:\n",
    "        return False\n",
    "    for i in range(2, int(n**0.5) + 1):\n",
    "        if n % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def factorial(n):\n",
    "    if n < 0:\n",
    "        return \"Undefined for negative numbers\"\n",
    "    result = 1\n",
    "    for i in range(1, n + 1):\n",
    "        result *= i\n",
    "    return result\n",
    "\n",
    "def fibonacci(n):\n",
    "    seq = []\n",
    "    a, b = 0, 1\n",
    "    for _ in range(n):\n",
    "        seq.append(a)\n",
    "        a, b = b, a + b\n",
    "    return seq"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a942e608-af6e-40d9-bb54-644bef15e426",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  5\n",
      "Enter operator (+, -, *, /):  +\n",
      "Enter second number:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 12.0\n"
     ]
    }
   ],
   "source": [
    "def calculator():\n",
    "    try:\n",
    "        num1 = float(input(\"Enter first number: \"))\n",
    "        operator = input(\"Enter operator (+, -, *, /): \")\n",
    "        num2 = float(input(\"Enter second number: \"))\n",
    "\n",
    "        if operator == '+':\n",
    "            print(\"Result:\", num1 + num2)\n",
    "        elif operator == '-':\n",
    "            print(\"Result:\", num1 - num2)\n",
    "        elif operator == '*':\n",
    "            print(\"Result:\", num1 * num2)\n",
    "        elif operator == '/':\n",
    "            try:\n",
    "                print(\"Result:\", num1 / num2)\n",
    "            except ZeroDivisionError:\n",
    "                print(\"Error: Cannot divide by zero.\")\n",
    "        else:\n",
    "            print(\"Error: Invalid operator. Use +, -, *, or /.\")\n",
    "\n",
    "    except ValueError:\n",
    "        print(\"Error: Please enter valid numbers.\")\n",
    "\n",
    "\n",
    "calculator()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c3e43daa-4668-4977-abf1-cf838b07948d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter file name:  yash\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: File not found. Please check the file name and try again.\n"
     ]
    }
   ],
   "source": [
    "filename = input(\"Enter file name: \")\n",
    "\n",
    "try:\n",
    "    with open(filename, 'r') as file:\n",
    "        for i in range(5):\n",
    "            line = file.readline()\n",
    "            if not line:\n",
    "                break \n",
    "            print(f\"Line {i + 1}: {line.strip()}\")\n",
    "except FileNotFoundError:\n",
    "    print(\"Error: File not found. Please check the file name and try again.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c5fe1212-6882-40c2-88c4-5869579c0c7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "questions.txt not found.\n"
     ]
    }
   ],
   "source": [
    "score = 0\n",
    "\n",
    "try:\n",
    "    with open(\"questions.txt\", \"r\") as file:\n",
    "        for line in file:\n",
    "            q, a = line.strip().split(\",\")\n",
    "            user_ans = input(q + \" \")\n",
    "            if user_ans.strip().lower() == a.strip().lower():\n",
    "                score += 1\n",
    "\n",
    "    with open(\"score.txt\", \"w\") as f:\n",
    "        f.write(\"Your score is: \" + str(score))\n",
    "    print(\"Your score is saved in 'score.txt'.\")\n",
    "\n",
    "except FileNotFoundError:\n",
    "    print(\"questions.txt not found.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a3d664d-478f-427f-88eb-4cecc22b3b67",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
