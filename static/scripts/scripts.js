// pega o modal

let id_suino;

var suinoModal = document.getElementById('suinoModal');
var div_grafico = document.getElementById('div_grafico')

suinoModal.addEventListener('show.bs.modal', async function (event) {
  // pega a linha <tr> que abriu o modal
  var row = event.relatedTarget;

  //  pega atributos data-* da tr ---
  var id = row.getAttribute('data-id');
  var peso = row.getAttribute('data-peso_inicial');
  var raca = row.getAttribute('data-raca');
  var tag = row.getAttribute('data-tag_suino');

  id_suino = id;

  // preenche os campos básicos do modal
  document.getElementById('suino-id').textContent = id;
  document.getElementById('suino-peso').textContent = peso;
  document.getElementById('suino-raca').textContent = raca;
  document.getElementById('suino-tag').textContent = tag;

  // buscar pesagens do backend ---
  var tbody = document.getElementById('pesagens-tbody'); // tabela dentro do modal
  tbody.innerHTML = '<tr><td colspan="3">Carregando...</td></tr>'; // feedback de loading

  try {
    // chama a rota do backend passando o id do suino
    const res = await fetch(`/api/buscar_pesagem/${id}`);

    if (!res.ok) throw new Error('Falha ao carregar dados (status ' + res.status + ')');

    const data = await res.json(); // pega JSON do servidor (lista de pesagens)
   

    if (!Array.isArray(data.pesagens) || data.pesagens.length === 0) {
      tbody.innerHTML = '<tr><td colspan="3" class="text-center">Nenhuma pesagem encontrada</td></tr>';
    } else {
      // monta a tabela de pesagens dinamicamente
      tbody.innerHTML = data.pesagens.map(p =>
        `<tr>
            <td>${p.peso}Kg</td>
            <td class="d-flex justify-content-evenly">${p.data}</td>
         </tr>`).join('');
    }
    if (!data.grafico || data.grafico.length === 0){
        div_grafico.innerHTML = "Erro ao carregar gráfico"
    }
    else{
        "<p>Gráfico Das Pesagens</p>"
        div_grafico.innerHTML = data.grafico

                // Seleciona e executa os scripts colados
        div_grafico.querySelectorAll("script").forEach(oldScript => {
          const newScript = document.createElement("script");
          
          if (oldScript.src) {
            
            newScript.src = oldScript.src;
          } else {
            
            newScript.textContent = oldScript.textContent;
          }
          
          document.body.appendChild(newScript);
          oldScript.remove();
        });
    }
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="3" class="text-center text-danger">Erro: ${err.message}</td></tr>`;
  }
});

function deletar_suino() {
  fetch(`/deletar_suino/${id_suino}`, {
    method: "POST" // ou DELETE se você preferir
  })
  .then(response => {
    if (response.ok) {
      console.log("Sucesso ao deletar suino");
      location.reload(); // recarrega a página para atualizar a tabela
    } else {
      console.log("Erro ao deletar suino");
    }
  })
  .catch(error => {
    console.error("Erro inesperado:", error);
  });
}


