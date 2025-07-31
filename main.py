import customtkinter as ctk
from tkinter import filedialog, messagebox
import requests
import threading
import os

# --- Dados dos Municípios (Reduzido para o exemplo) ---
# Adicione todos os outros municípios a esta lista para preenchê-la.
municipios_lista = [
    'TODOS',
    'Abaíra - 2900108',
    'Abaré - 2900207',
    'Acajutiba - 2900306',
    'Adustina - 2900355',
    'Água Fria - 2900405',
    'Aiquara - 2900603',
    'Alagoinhas - 2900702',
    'Alcobaça - 2900801',
    'Almadina - 2900900',
    'Amargosa - 2901007',
    'Amélia Rodrigues - 2901106',
    'América Dourada - 2901155',
    'Anagé - 2901205',
    'Andaraí - 2901304',
    'Andorinha - 2901353',
    'Angical - 2901403',
    'Anguera - 2901502',
    'Antas - 2901601',
    'Antônio Cardoso - 2901700',
    'Antônio Gonçalves - 2901809',
    'Aporá - 2901908',
    'Apuarema - 2901957',
    'Araçás - 2902054',
    'Aracatu - 2902005',
    'Araci - 2902104',
    'Aramari - 2902203',
    'Arataca - 2902252',
    'Aratuípe - 2902302',
    'Aurelino Leal - 2902401',
    'Baianópolis - 2902500',
    'Baixa Grande - 2902609',
    'Banzaê - 2902658',
    'Barra - 2902708',
    'Barra da Estiva - 2902807',
    'Barra do Choça - 2902906',
    'Barra do Mendes - 2903003',
    'Barra do Rocha - 2903102',
    'Barreiras - 2903201',
    'Barro Alto - 2903235',
    'Barro Preto - 2903300',
    'Barrocas - 2903276',
    'Belmonte - 2903409',
    'Belo Campo - 2903508',
    'Biritinga - 2903607',
    'Boa Nova - 2903706',
    'Boa Vista do Tupim - 2903805',
    'Bom Jesus da Lapa - 2903904',
    'Bom Jesus da Serra - 2903953',
    'Boninal - 2904001',
    'Bonito - 2904050',
    'Boquira - 2904100',
    'Botuporã - 2904209',
    'Brejões - 2904308',
    'Brejolândia - 2904407',
    'Brotas de Macaúbas - 2904506',
    'Brumado - 2904605',
    'Buerarema - 2904704',
    'Buritirama - 2904753',
    'Caatiba - 2904803',
    'Cabaceiras do Paraguaçu - 2904852',
    'Cachoeira - 2904902',
    'Caculé - 2905008',
    'Caém - 2905107',
    'Caetanos - 2905156',
    'Caetité - 2905206',
    'Cafarnaum - 2905305',
    'Cairu - 2905404',
    'Caldeirão Grande - 2905503',
    'Camacan - 2905602',
    'Camaçari - 2905701',
    'Camamu - 2905800',
    'Campo Alegre de Lourdes - 2905909',
    'Campo Formoso - 2906006',
    'Canápolis - 2906105',
    'Canarana - 2906204',
    'Canavieiras - 2906303',
    'Candeal - 2906402',
    'Candeias - 2906501',
    'Candiba - 2906600',
    'Cândido Sales - 2906709',
    'Cansanção - 2906808',
    'Canudos - 2906824',
    'Capela do Alto Alegre - 2906857',
    'Capim Grosso - 2906873',
    'Caraíbas - 2906899',
    'Caravelas - 2906907',
    'Cardeal da Silva - 2907004',
    'Carinhanha - 2907103',
    'Casa Nova - 2907202',
    'Castro Alves - 2907301',
    'Catolândia - 2907400',
    'Catu - 2907509',
    'Caturama - 2907558',
    'Central - 2907608',
    'Chorrochó - 2907707',
    'Cícero Dantas - 2907806',
    'Cipó - 2907905',
    'Coaraci - 2908002',
    'Cocos - 2908101',
    'Conceição da Feira - 2908200',
    'Conceição do Almeida - 2908309',
    'Conceição do Coité - 2908408',
    'Conceição do Jacuípe - 2908507',
    'Conde - 2908606',
    'Condeúba - 2908705',
    'Contendas do Sincorá - 2908804',
    'Coração de Maria - 2908903',
    'Cordeiros - 2909000',
    'Coribe - 2909109',
    'Coronel João Sá - 2909208',
    'Correntina - 2909307',
    'Cotegipe - 2909406',
    'Cravolândia - 2909505',
    'Crisópolis - 2909604',
    'Cristópolis - 2909703',
    'Cruz das Almas - 2909802',
    'Curaçá - 2909901',
    'Dário Meira - 2910008',
    "Dias D'Ávila - 2910057",
    'Dom Basílio - 2910107',
    'Dom Macedo Costa - 2910206',
    'Elísio Medrado - 2910305',
    'Encruzilhada - 2910404',
    'Entre Rios - 2910503',
    'Érico Cardoso - 2900504',
    'Esplanada - 2910602',
    'Euclides da Cunha - 2910701',
    'Eunápolis - 2910727',
    'Fátima - 2910750',
    'Feira da Mata - 2910776',
    'Feira de Santana - 2910800',
    'Filadélfia - 2910859',
    'Firmino Alves - 2910909',
    'Floresta Azul - 2911006',
    'Formosa do Rio Preto - 2911105',
    'Gandu - 2911204',
    'Gavião - 2911253',
    'Gentio do Ouro - 2911303',
    'Glória - 2911402',
    'Gongogi - 2911501',
    'Governador Mangabeira - 2911600',
    'Guajeru - 2911659',
    'Guanambi - 2911709',
    'Guaratinga - 2911808',
    'Heliópolis - 2911857',
    'Iaçu - 2911907',
    'Ibiassucê - 2912004',
    'Ibicaraí - 2912103',
    'Ibicoara - 2912202',
    'Ibicuí - 2912301',
    'Ibipeba - 2912400',
    'Ibipitanga - 2912509',
    'Ibiquera - 2912608',
    'Ibirapitanga - 2912707',
    'Ibirapuã - 2912806',
    'Ibirataia - 2912905',
    'Ibitiara - 2913002',
    'Ibititá - 2913101',
    'Ibotirama - 2913200',
    'Ichu - 2913309',
    'Igaporã - 2913408',
    'Igrapiúna - 2913457',
    'Iguaí - 2913507',
    'Ilhéus - 2913606',
    'Inhambupe - 2913705',
    'Ipecaetá - 2913804',
    'Ipiaú - 2913903',
    'Ipirá - 2914000',
    'Ipupiara - 2914109',
    'Irajuba - 2914208',
    'Iramaia - 2914307',
    'Iraquara - 2914406',
    'Irará - 2914505',
    'Irecê - 2914604',
    'Itabela - 2914653',
    'Itaberaba - 2914703',
    'Itabuna - 2914802',
    'Itacaré - 2914901',
    'Itaetê - 2915007',
    'Itagi - 2915106',
    'Itagibá - 2915205',
    'Itagimirim - 2915304',
    'Itaguaçu da Bahia - 2915353',
    'Itaju do Colônia - 2915403',
    'Itajuípe - 2915502',
    'Itamaraju - 2915601',
    'Itamari - 2915700',
    'Itambé - 2915809',
    'Itanagra - 2915908',
    'Itanhém - 2916005',
    'Itaparica - 2916104',
    'Itapé - 2916203',
    'Itapebi - 2916302',
    'Itapetinga - 2916401',
    'Itapicuru - 2916500',
    'Itapitanga - 2916609',
    'Itaquara - 2916708',
    'Itarantim - 2916807',
    'Itatim - 2916856',
    'Itiruçu - 2916906',
    'Itiúba - 2917003',
    'Itororó - 2917102',
    'Ituaçu - 2917201',
    'Ituberá - 2917300',
    'Iuiu - 2917334',
    'Jaborandi - 2917359',
    'Jacaraci - 2917409',
    'Jacobina - 2917508',
    'Jaguaquara - 2917607',
    'Jaguarari - 2917706',
    'Jaguaripe - 2917805',
    'Jandaíra - 2917904',
    'Jequié - 2918001',
    'Jeremoabo - 2918100',
    'Jiquiriçá - 2918209',
    'Jitaúna - 2918308',
    'João Dourado - 2918357',
    'Juazeiro - 2918407',
    'Jucuruçu - 2918456',
    'Jussara - 2918506',
    'Jussari - 2918555',
    'Jussiape - 2918605',
    'Lafayette Coutinho - 2918704',
    'Lagoa Real - 2918753',
    'Laje - 2918803',
    'Lajedão - 2918902',
    'Lajedinho - 2919009',
    'Lajedo do Tabocal - 2919058',
    'Lamarão - 2919108',
    'Lapão - 2919157',
    'Lauro de Freitas - 2919207',
    'Lençóis - 2919306',
    'Licínio de Almeida - 2919405',
    'Livramento de Nossa Senhora - 2919504',
    'Luís Eduardo Magalhães - 2919553',
    'Macajuba - 2919603',
    'Macarani - 2919702',
    'Macaúbas - 2919801',
    'Macururé - 2919900',
    'Madre de Deus - 2919926',
    'Maetinga - 2919959',
    'Maiquinique - 2920007',
    'Mairi - 2920106',
    'Malhada - 2920205',
    'Malhada de Pedras - 2920304',
    'Manoel Vitorino - 2920403',
    'Mansidão - 2920452',
    'Maracás - 2920502',
    'Maragogipe - 2920601',
    'Maraú - 2920700',
    'Marcionílio Souza - 2920809',
    'Mascote - 2920908',
    'Mata de São João - 2921005',
    'Matina - 2921054',
    'Medeiros Neto - 2921104',
    'Miguel Calmon - 2921203',
    'Milagres - 2921302',
    'Mirangaba - 2921401',
    'Mirante - 2921450',
    'Monte Santo - 2921500',
    'Morpará - 2921609',
    'Morro do Chapéu - 2921708',
    'Mortugaba - 2921807',
    'Mucugê - 2921906',
    'Mucuri - 2922003',
    'Mulungu do Morro - 2922052',
    'Mundo Novo - 2922102',
    'Muniz Ferreira - 2922201',
    'Muquém do São Francisco - 2922250',
    'Muritiba - 2922300',
    'Mutuípe - 2922409',
    'Nazaré - 2922508',
    'Nilo Peçanha - 2922607',
    'Nordestina - 2922656',
    'Nova Canaã - 2922706',
    'Nova Fátima - 2922730',
    'Nova Ibiá - 2922755',
    'Nova Itarana - 2922805',
    'Nova Redenção - 2922854',
    'Nova Soure - 2922904',
    'Nova Viçosa - 2923001',
    'Novo Horizonte - 2923035',
    'Novo Triunfo - 2923050',
    'Olindina - 2923100',
    'Oliveira dos Brejinhos - 2923209',
    'Ouriçangas - 2923308',
    'Ourolândia - 2923357',
    'Palmas de Monte Alto - 2923407',
    'Palmeiras - 2923506',
    'Paramirim - 2923605',
    'Paratinga - 2923704',
    'Paripiranga - 2923803',
    'Pau-Brasil - 2923902',
    'Paulo Afonso - 2924009',
    'Pé de Serra - 2924058',
    'Pedrão - 2924108',
    'Pedro Alexandre - 2924207',
    'Piatã - 2924306',
    'Pilão Arcado - 2924405',
    'Pindaí - 2924504',
    'Pindobaçu - 2924603',
    'Pintadas - 2924652',
    'Piraí do Norte - 2924678',
    'Piripá - 2924702',
    'Piritiba - 2924801',
    'Planaltino - 2924900',
    'Planalto - 2925006',
    'Poções - 2925105',
    'Pojuca - 2925204',
    'Ponto Novo - 2925253',
    'Porto Seguro - 2925303',
    'Potiraguá - 2925402',
    'Prado - 2925501',
    'Presidente Dutra - 2925600',
    'Presidente Jânio Quadros - 2925709',
    'Presidente Tancredo Neves - 2925758',
    'Queimadas - 2925808',
    'Quijingue - 2925907',
    'Quixabeira - 2925931',
    'Rafael Jambeiro - 2925956',
    'Remanso - 2926004',
    'Retirolândia - 2926103',
    'Riachão das Neves - 2926202',
    'Riachão do Jacuípe - 2926301',
    'Riacho de Santana - 2926400',
    'Ribeira do Amparo - 2926509',
    'Ribeira do Pombal - 2926608',
    'Ribeirão do Largo - 2926657',
    'Rio de Contas - 2926707',
    'Rio do Antônio - 2926806',
    'Rio do Pires - 2926905',
    'Rio Real - 2927002',
    'Rodelas - 2927101',
    'Ruy Barbosa - 2927200',
    'Salinas da Margarida - 2927309',
    'Salvador - 2927408',
    'Santa Bárbara - 2927507',
    'Santa Brígida - 2927606',
    'Santa Cruz Cabrália - 2927705',
    'Santa Cruz da Vitória - 2927804',
    'Santa Inês - 2927903',
    'Santa Luzia - 2928059',
    'Santa Maria da Vitória - 2928109',
    'Santa Rita de Cássia - 2928406',
    'Santa Terezinha - 2928505',
    'Santaluz - 2928000',
    'Santana - 2928208',
    'Santanópolis - 2928307',
    'Santo Amaro - 2928604',
    'Santo Antônio de Jesus - 2928703',
    'Santo Estêvão - 2928802',
    'São Desidério - 2928901',
    'São Domingos - 2928950',
    'São Felipe - 2929107',
    'São Félix - 2929008',
    'São Félix do Coribe - 2929057',
    'São Francisco do Conde - 2929206',
    'São Gabriel - 2929255',
    'São Gonçalo dos Campos - 2929305',
    'São José da Vitória - 2929354',
    'São José do Jacuípe - 2929370',
    'São Miguel das Matas - 2929404',
    'São Sebastião do Passé - 2929503',
    'Sapeaçu - 2929602',
    'Sátiro Dias - 2929701',
    'Saubara - 2929750',
    'Saúde - 2929800',
    'Seabra - 2929909',
    'Sebastião Laranjeiras - 2930006',
    'Senhor do Bonfim - 2930105',
    'Sento Sé - 2930204',
    'Serra do Ramalho - 2930154',
    'Serra Dourada - 2930303',
    'Serra Preta - 2930402',
    'Serrinha - 2930501',
    'Serrolândia - 2930600',
    'Simões Filho - 2930709',
    'Sítio do Mato - 2930758',
    'Sítio do Quinto - 2930766',
    'Sobradinho - 2930774',
    'Souto Soares - 2930808',
    'Tabocas do Brejo Velho - 2930907',
    'Tanhaçu - 2931004',
    'Tanque Novo - 2931053',
    'Tanquinho - 2931103',
    'Taperoá - 2931202',
    'Tapiramutá - 2931301',
    'Teixeira de Freitas - 2931350',
    'Teodoro Sampaio - 2931400',
    'Teofilândia - 2931509',
    'Teolândia - 2931608',
    'Terra Nova - 2931707',
    'Tremedal - 2931806',
    'Tucano - 2931905',
    'Uauá - 2932002',
    'Ubaíra - 2932101',
    'Ubaitaba - 2932200',
    'Ubatã - 2932309',
    'Uibaí - 2932408',
    'Umburanas - 2932457',
    'Una - 2932507',
    'Urandi - 2932606',
    'Uruçuca - 2932705',
    'Utinga - 2932804',
    'Valença - 2932903',
    'Valente - 2933000',
    'Várzea da Roça - 2933059',
    'Várzea do Poço - 2933109',
    'Várzea Nova - 2933158',
    'Varzedo - 2933174',
    'Vera Cruz - 2933208',
    'Vereda - 2933257',
    'Vitória da Conquista - 2933307',
    'Wagner - 2933406',
    'Wanderley - 2933455',
    'Wenceslau Guimarães - 2933505',
    'Xique-Xique - 2933604',
]

# Lista para guardar a referência dos botões de rádio
radio_buttons = []


# --- Funções de Lógica da Aplicação (sem alterações aqui) ---

def iniciar_download():
    selecao = radio_var.get()

    if selecao == "TODOS":
        folder_path = filedialog.askdirectory(title="Escolha uma pasta para salvar todos os mapas")
        if not folder_path:
            messagebox.showwarning("Aviso", "Nenhuma pasta foi selecionada. Operação cancelada.")
            return

        set_widgets_state("disabled")
        thread = threading.Thread(target=baixar_todos_os_mapas, args=(folder_path,))
        thread.start()

    else:
        try:
            codigo = selecao.split(' - ')[-1]
        except IndexError:
            messagebox.showerror("Erro", "Seleção inválida.")
            return

        nome_arquivo_sugerido = f"mapa_com_descritivo_atual_{codigo}.pdf"
        filepath = filedialog.asksaveasfilename(
            initialfile=nome_arquivo_sugerido,
            defaultextension=".pdf",
            filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*")],
            title="Salvar mapa como..."
        )
        if not filepath:
            messagebox.showwarning("Aviso", "Nenhum local de salvamento foi escolhido. Operação cancelada.")
            return

        set_widgets_state("disabled")
        url = f"https://ftp.sei.ba.gov.br/Geoinformacao/mapas/munic/vigente/{nome_arquivo_sugerido}"
        thread = threading.Thread(target=baixar_mapa_unico, args=(url, filepath))
        thread.start()


def baixar_mapa_unico(url, filepath):
    status_label.configure(text=f"Baixando: {os.path.basename(filepath)}...")
    progress_bar.configure(mode="indeterminate")
    progress_bar.start()

    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        status_label.configure(text="Download concluído com sucesso!")
        messagebox.showinfo("Sucesso", f"Mapa salvo em:\n{filepath}")

    except requests.exceptions.RequestException as e:
        status_label.configure(text="Erro no download.")
        messagebox.showerror("Erro no Download", f"Não foi possível baixar o arquivo: {e}")
    finally:
        set_widgets_state("normal")
        progress_bar.stop()
        progress_bar.set(0)


def baixar_todos_os_mapas(folder_path):
    total_mapas = len(municipios_lista) - 1
    progress_bar.configure(mode="determinate")

    for i, item in enumerate(municipios_lista[1:]):
        codigo = item.split(' - ')[-1]
        nome_arquivo = f"mapa_com_descritivo_atual_{codigo}.pdf"
        filepath = os.path.join(folder_path, nome_arquivo)
        url = f"https://ftp.sei.ba.gov.br/Geoinformacao/mapas/munic/vigente/{nome_arquivo}"

        status_label.configure(text=f"Baixando {i + 1}/{total_mapas}: {nome_arquivo}...")
        progress_bar.set((i + 1) / total_mapas)
        app.update_idletasks()

        try:
            response = requests.get(url, stream=True, timeout=30)
            if response.status_code == 404:
                print(f"Arquivo não encontrado para o código {codigo}, pulando.")
                continue
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                f.write(response.content)

        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar mapa para o código {codigo}: {e}")
            continue

    status_label.configure(text="Processo finalizado!")
    set_widgets_state("normal")
    progress_bar.set(1)
    messagebox.showinfo("Concluído", f"Download de todos os mapas finalizado.\nVerifique a pasta: {folder_path}")
    progress_bar.set(0)


# --- FUNÇÃO CORRIGIDA ---
def set_widgets_state(state):
    """Habilita ou desabilita os widgets interativos."""
    # Desabilita o botão de download
    download_button.configure(state=state)

    # Itera sobre cada botão de rádio na lista e altera seu estado
    for button in radio_buttons:
        button.configure(state=state)


# --- Configuração da Interface Gráfica ---

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Baixar Mapas Municipais da Bahia - SEI")
app.geometry("550x500")

main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

label_lista = ctk.CTkLabel(main_frame, text="Escolha um Município na lista abaixo:",
                           font=ctk.CTkFont(size=14, weight="bold"))
label_lista.pack(padx=20, pady=(20, 10), anchor="w")

radio_var = ctk.StringVar(value="TODOS")
scrollable_frame = ctk.CTkScrollableFrame(main_frame, height=200)
scrollable_frame.pack(padx=20, pady=0, fill="x")

# Loop para criar os botões e ADICIONÁ-LOS A UMA LISTA DE REFERÊNCIA
for item in municipios_lista:
    radio_button = ctk.CTkRadioButton(
        master=scrollable_frame,
        text=item,
        variable=radio_var,
        value=item
    )
    radio_button.pack(padx=10, pady=5, anchor="w")
    radio_buttons.append(radio_button)  # <-- Adicionamos o botão à lista

download_button = ctk.CTkButton(main_frame, text="Baixar Mapa(s)", command=iniciar_download,
                                font=ctk.CTkFont(size=14, weight="bold"))
download_button.pack(padx=20, pady=20, ipady=8, fill="x")

status_label = ctk.CTkLabel(main_frame, text="", font=ctk.CTkFont(size=12))
status_label.pack(padx=20, pady=0)

progress_bar = ctk.CTkProgressBar(main_frame)
progress_bar.set(0)
progress_bar.pack(padx=20, pady=(5, 20), fill="x")

app.mainloop()