# Zeus Haberlesme Sistemi

Kendi sunucunuzu ve istemcinizi kullanarak dünyanın her yerinden herkesle sohbet edin.

## Kurulum ve Başlangıç

### Not:
TCP bağlantısı için kredi kartı doğrulaması yapmanız gerekebilir. Kredi kartı doğrulaması için [Ngrok'un ödeme sayfasını](https://dashboard.ngrok.com/billing) ziyaret edebilirsiniz.


### 1. Ngrok Hesabı Oluşturma ve Authtoken Alma

1. **Ngrok Hesabı Oluşturun:**
   - [Ngrok](https://ngrok.com) web sitesine gidin ve bir hesap oluşturun.

2. **Ngrok Authtoken'unuzu Alın:**
   - Ngrok hesabınıza giriş yaptıktan sonra, kullanıcı panelinizde "Auth Tokens" bölümüne gidin ve `Authtoken`'ınızı kopyalayın.

### 2. Ngrok Authtoken'u Terminale Ekleyin

1. **Terminali Açın:**
   - Bilgisayarınızda bir terminal veya komut istemcisi açın.

2. **Ngrok Authtoken'unuzu Ekleyin:**
   - Terminale şu komutu yazın:
     ```bash
     python install.py
     ```
   - Ardından, kopyaladığınız `Authtoken`'ı girin ve kurulum işlemini tamamlayın.

### 3. PUB_CON.py Dosyasını Düzenleme

1. **Ngrok URL Ekleme:**
   - `PUB_CON.py` dosyasının 17. satırında bulunan `get_data_url = ""` kısmındaki parantez içine, Ngrok'un size sağladığı URL'yi girin.
   
     ```python
     get_data_url = "ngrok_url"
     ```

### 4. Tool'u Başlatma

1. **Tool'u Başlatın:**
   - Terminale şu komutu yazın:
     ```bash
     python3 trchat.py
     ```
   - Bu komut, tool'unuzu başlatacaktır.

### Tool Kullanımı

Tool başlatıldığında iki seçenekle karşılaşacaksınız:

#### 1. Start Server
- **Açıklama:** Bu seçeneği seçerseniz, size ait bir sunucu odası oluşturulur ve bir güvenlik anahtarına sahip olursunuz. Bu anahtarı diğer kişilere vererek onların sunucunuza bağlanmasını sağlayabilirsiniz.
  
  ![Start Server Ekran Görüntüsü](https://github.com/user-attachments/assets/7c7acf19-2724-4e6d-a718-3b0f928da989)
  *Tool'un Start Server seçeneğini gösteren ekran görüntüsü.*

#### 2. Connect with Server
- **Açıklama:** Bu seçeneği seçerseniz, bir kullanıcı adı oluşturmanız ve bağlanmak istediğiniz sunucunun güvenlik anahtarını girmeniz gerekecektir. Sunucuya bağlanarak sohbet edebilirsiniz.

  ![Connect with Server Ekran Görüntüsü](https://github.com/user-attachments/assets/72348904-9ef5-4133-b5da-976fcfd1d2fb)
  *Tool'un Connect with Server seçeneğini gösteren ekran görüntüsü.*

## Görseller

Aşağıda tool'un farklı bölümlerini gösteren ekran görüntüleri bulunmaktadır:

1. **Ngrok Authtoken Ekleme:**
   ![Ngrok Authtoken Ekran Görüntüsü](https://github.com/user-attachments/assets/95216e46-9f7e-4546-959d-af6cc5ab9fb2)

2. **Tool Arayüzü:**
   ![Tool Başlatma Ekran Görüntüsü](https://github.com/user-attachments/assets/1a70c6b9-c444-4026-9836-f8fa3d19a149)

   
