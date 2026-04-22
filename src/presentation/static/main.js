let currentMode = 'encrypt';

function switchMode(mode) {
    currentMode = mode;
    document.getElementById('tab-encrypt').classList.toggle('active', mode === 'encrypt');
    document.getElementById('tab-decrypt').classList.toggle('active', mode === 'decrypt');
    
    document.getElementById('input-label').innerText = mode === 'encrypt' 
        ? 'Digite o texto para criptografar:' 
        : 'Cole os emojis para descriptografar:';
        
    document.getElementById('input-text').placeholder = mode === 'encrypt'
        ? 'Ex: Ola mundo'
        : 'Ex: 🍎🍌🐱';

    document.getElementById('input-text').value = '';
    hideResult();
}

function hideResult() {
    const box = document.getElementById('result-box');
    box.classList.remove('visible');
    setTimeout(() => {
        box.innerHTML = '<span class="empty-state">O resultado aparecerá aqui...</span>';
        box.classList.add('visible');
    }, 300);
}

async function process() {
    const input = document.getElementById('input-text').value;
    if (!input) return;

    const endpoint = currentMode === 'encrypt' ? '/encrypt' : '/decrypt';
    const payload = currentMode === 'encrypt' ? { text: input } : { emojis: input };

    const btn = document.getElementById('action-btn');
    const originalText = btn.innerText;
    btn.innerText = 'Processando... ⏳';

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        
        const box = document.getElementById('result-box');
        box.classList.remove('visible');
        
        setTimeout(() => {
            if (data.result === "") {
                box.innerHTML = '<span class="empty-state">Nenhum caractere válido encontrado.</span>';
            } else {
                box.innerText = data.result || data.error;
            }
            box.classList.add('visible');
        }, 300);

    } catch (error) {
        alert('Erro ao conectar com o servidor.');
    } finally {
        btn.innerText = originalText;
    }
}
