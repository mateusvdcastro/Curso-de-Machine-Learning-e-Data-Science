# Curso de Machine Learning e Data Science
## Descrição
---
Estudos sobre **Ml** e __Data Science__

---

### Treinando Marckdown

![249ae1594d75fdd0f33bdea2a40ac736](https://user-images.githubusercontent.com/86390161/135910709-15f87e28-13b1-40ce-9047-dde9f90b48ec.jpg)

[Acesse minha página sobre a assunto:](https://instagram.com/python_overview)

Data Science
1. Visualização de dados
   1. Matplotlib
   2. Seaborn
   3. Plotly
   4. Pyplot
2. Matemática
   1. Numpy
   1. Math
   1. Pandas

Machine Learning
1. Sckit-learn  
2. Tensor Flow
3. Keras

Num | Nome | Nota
---|---|---
1|Ricardo|8,5
2|Anailson|9

`from sklearn import train_test_split`

```
class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='Email')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário', blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.nome_comentario
```
:japanese_goblin: :ghost: :robot: :boom: :heart: :+1: :-1: :horse_racing:

> Citando uma pessoa 

