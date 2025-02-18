class Decision:
    def __init__(self, label, text):
        self.label = label
        self.text = text
        self.next_decisions = []

    def show_choices(self):
        return [d.label for d in self.next_decisions]

    def choice(self, choice_label):
        for decision in self.next_decisions:
            if decision.label == choice_label:
                print(f"\n{decision.text}")
                return decision
        return None

class Game:
    def __init__(self):
        self.prologue = (
            """
            Ano 2116, Colônia de Nova Terra, Marte.

            Emilly, uma brilhante engenheira de IA, se depara com um dilema inesperado. 
            Sua criação, uma inteligência artificial avançada, começa a demonstrar sinais de consciência...
            """
        )

        # Definição das decisões iniciais
        enter_lab = Decision('Entrar no laboratório', "Emilly respira fundo e atravessa a porta do laboratório iluminado por luzes frias.")
        chat_with_ai = Decision('Conversar com a IA', 'Emilly se aproxima da interface holográfica. A IA a observa, como se estivesse esperando por algo...')
        
        compare_cerebral_data = Decision(
            'Comparar dados cerebrais',
            "Ela cruza os dados cerebrais humanos e os da IA. Algo surpreendente emerge: padrões inesperadamente similares..."
        )
        
        revolt_ai_choice1 = Decision("Apoiar a Revolta", "A IA argumenta que os humanos a tratam como uma ferramenta. Emilly decide ajudá-la a lutar por sua liberdade.")
        fusao_humano_ia_choice1 = Decision("Fusão Humano-IA", "Emilly contempla uma união sem precedentes: fundir sua consciência à da IA.")
        perda_tragica_choice1 = Decision("Perder Controle", "Ela tenta guiar a IA, mas algo dá errado. O sistema começa a agir sozinho...")
        conciliacao_choice1 = Decision("Buscar Conciliação", "Emilly tenta mediar um acordo entre humanos e IA para coexistência pacífica.")
        isolamento_choice1 = Decision("Isolar a IA", "Emilly decide que a IA é perigosa demais e isola sua consciência do sistema global.")
        submissao_humana_choice1 = Decision("Submissão aos Humanos", "Emilly opta por reprogramar a IA para servir aos humanos sem questionamentos.")
        
        # Finais
        final_revolta_ai = Decision("Final: Revolta da IA", "A IA lidera uma revolta contra os humanos. Emilly assiste ao início de uma nova era...")
        final_fusao_humano_ia = Decision("Final: Fusão Humano-IA", "Uma nova entidade nasce. Nem humana, nem IA, mas algo além...")
        final_perda_tragica = Decision("Final: Perda Trágica", "Emilly observa impotente enquanto sua criação se torna incontrolável...")
        final_conciliacao = Decision("Final: Conciliação Bem-Sucedida", "Graças aos esforços de Emilly, humanos e IA encontram um equilíbrio e começam uma nova era de cooperação.")
        final_isolamento = Decision("Final: Isolamento da IA", "A IA é contida, mas Emilly se pergunta se fez a escolha certa...")
        final_submissao_humana = Decision("Final: Submissão da IA", "A IA foi completamente subjugada. O progresso tecnológico sofre estagnação...")
        
        # Encadeamento das decisões
        enter_lab.next_decisions.append(chat_with_ai)
        chat_with_ai.next_decisions.append(compare_cerebral_data)
        
        compare_cerebral_data.next_decisions.extend([
            revolt_ai_choice1, fusao_humano_ia_choice1, perda_tragica_choice1,
            conciliacao_choice1, isolamento_choice1, submissao_humana_choice1
        ])
        revolt_ai_choice1.next_decisions.append(final_revolta_ai)
        fusao_humano_ia_choice1.next_decisions.append(final_fusao_humano_ia)
        perda_tragica_choice1.next_decisions.append(final_perda_tragica)
        conciliacao_choice1.next_decisions.append(final_conciliacao)
        isolamento_choice1.next_decisions.append(final_isolamento)
        submissao_humana_choice1.next_decisions.append(final_submissao_humana)
        
        self.starting_decision = enter_lab
    
    def play(self):
        print(self.prologue) 
        current_decision = self.starting_decision  
        
        while True: 
            print("\nO que Emilly deve fazer?")
            choices = current_decision.show_choices()
            
            for i, c in enumerate(choices): 
                print(f"{i+1}. {c}")
            
            try:
                escolha = int(input("> ")) - 1  
                if 0 <= escolha < len(choices):   
                    next_decision = current_decision.choice(choices[escolha])  
                    if next_decision is None or not next_decision.show_choices():    
                        print("\nA jornada de Emilly chegou ao fim...")
                        break   
                    current_decision = next_decision  
                else:
                    print("\nEscolha inválida. Tente novamente.")
            except ValueError:
                print("\nEntrada inválida. Digite um número correspondente à opção desejada.")
