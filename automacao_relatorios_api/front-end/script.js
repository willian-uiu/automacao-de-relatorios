document.addEventListener('DOMContentLoaded', () => {
    
    const form = document.getElementById('solicitacao-form');
    const setorSelect = document.getElementById('setor-select');
    const revendaInput = document.getElementById('revenda-input'); // <-- Pega a referência do novo campo
    const alertPlaceholder = document.getElementById('alert-placeholder');

    const API_URL = 'http://127.0.0.1:8000/solicitacoes';

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const setorId = setorSelect.value;
        const revendaId = revendaInput.value; // <-- Lê o valor do campo de revenda

        // Pequena validação para garantir que o campo não está vazio
        if (!revendaId.trim()) {
            showAlert('Por favor, insira o ID da Revenda.', 'warning');
            return;
        }

        const requestBody = {
            revenda_id: revendaId,
            setor_id: setorId
        };

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody),
            });

            const data = await response.json();

            if (response.ok) {
                showAlert(`Solicitação para revenda ${data.revenda_id} e setor ${data.setor_id} criada com sucesso! (ID: ${data.id})`, 'success');
            } else {
                showAlert(`Erro: ${data.detail}`, 'danger');
            }

        } catch (error) {
            console.error('Erro de conexão:', error);
            showAlert('Não foi possível conectar à API.', 'danger');
        }
    });

    const showAlert = (message, type) => {
        const wrapper = document.createElement('div');
        wrapper.innerHTML = [
            `<div class="alert alert-${type} alert-dismissible" role="alert">`,
            `   <div>${message}</div>`,
            '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
            '</div>'
        ].join('');
        alertPlaceholder.innerHTML = ''; 
        alertPlaceholder.append(wrapper);
    }
});

const bootstrapScript = document.createElement('script');
bootstrapScript.src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js';
document.body.appendChild(bootstrapScript);