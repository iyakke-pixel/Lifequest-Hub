document.getElementById('calc-split-btn').addEventListener('click', () => {
  const name = document.getElementById('bill-name').value || 'Bill';
  const amount = parseFloat(document.getElementById('bill-amount').value);
  const people = parseInt(document.getElementById('people-count').value) || 1;

  if (!amount || amount <= 0) return alert('Enter a valid bill amount.');

  const perPerson = (amount / people).toFixed(2);
  const res = document.getElementById('split-result');
  res.classList.remove('hidden');
  res.textContent = `💡 ${name}: $${amount.toFixed(2)} total ➔ Each person owes $${perPerson}`;
});