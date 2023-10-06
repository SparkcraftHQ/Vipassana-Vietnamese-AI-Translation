import streamlit as st
import requests
# from langchain.llms import OpenAI
st.set_page_config(page_title="🧘‍♀️ Vipassana English to Vietnamese AI Translation")
st.title('🧘‍♀️ Vipassana English to Vietnamese AI Translation')

# openai_api_key = st.sidebar.text_input('OpenAI API Key')

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=651c7b1947d3f5121922ef3f&org=ea64a3cc-e2b2-457c-b270-fa0555e9f477"
headers = {'Authorization':
      'Bearer 3e5b03f4-74c3-470c-bc45-f5318c10c3b0',
      'Content-Type': 'application/json'
    }

def generate_response(input_text, input_dictionary):
  # llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  payload = {
    "in-0":input_text,
    "in-1": input_dictionary
  }
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()

st.info('''This AI uses GPT4 AI behind the scenes, it learned the Pali to Vietnamese Dictionary from https://www.budsas.org/uni/u-dainiemxu/dnx09.htm. 
        
All you need to do is to paste the english text and then press submit button and wait for few minutes, it will generate the translation in Vietnamese. 
        
Please note that this AI takes up to 8,000 English words at a time. 
        
Please also note that because this is a free service, this AI can only do 100 translations per month.
        
This AI App was made with love and kindness by Tuyen Nguyen and Tianyu Guo.''')



with st.form('my_form'):
  
  dictionary = st.text_area('Add more word definitions into Dictionary:', '''[A]

Abhidhammaa: Vi Diệu Pháp; Thắng Pháp; những giáo pháp cao thượng của Ðức Phật; tạng thứ ba trong Tam Tạng Paa.li; triết học và tâm lý học Phật giáo; siêu hình học Phật giáo, giải thích sự vật theo chân đế.

Abhi~n~naa: Thần thông; thắng trí; năng lực siêu nhiên.

Abhirati: Người có sự thích thú về một thứ gì đó, như thích thú và nhiệt thành trong giáo pháp chẳng hạn; dùng để chỉ người hành thiền với mục đích được hưởng dục lạc ngũ trần trong các kiếp sau.

Akusala: Bất thiện; ác; tội lỗi.

Aalaara Kaalaama: Một thiền sư nổi tiếng thời Ðức Phật, một trong hai vị thầy của Bồ tát Sĩ Ðạt Ta.

Anaagaami: A-na-hàm; Bất lai; vị đắc tầng thánh thứ ba, không còn tái sanh vào cảnh dục giới, hoàn toàn loại trừ sân hận và tham ái ngũ dục; nhưng còn các phiền não vi tế như: luyến ái cảnh sắc giới, luyến ái cảnh vô sắc giới, ngã mạn, phóng dật và vô minh.

Anaagaarika: Người hộ tăng. Trong các xứ Phật giáo, người hộ tăng giữ tám giới hay mười giới, thường mặc đồ trắng, sống trong chùa phụ giúp cho tăng, ni.

Aanaapaana-sati: Niệm hơi thở.

Anatta: Vô ngã, phi ngã, không có tự ngã, không có bản chất, không đáp ứng được sự mong ước của`con người. Một trong Tam tướng: vô thường, khổ, vô ngã.

Anatta lakkhanaa: Ðặc tính hay tướng vô ngã. Hiện tượng vượt ngoài khả năng kiểm soát.

Anattaa-nupassanaa-~naana: Tuệ giác thấy được sự vô ngã. Trực giác được rằng không ai có thể điều khiển, kiểm soát.

Anicca: Vô thường.

Anicca lakkhanaa: Ðặc tính hay tướng vô thường. Hiện tượng sinh diệt của các pháp.

Aniccaa-nupassanaa-~naana: Tuệ giác thấy được sự vô thường. Trực giác được sự diệt tận nhanh chóng của các pháp.

Anuggahita: Bảo vệ, đặc biệt cho việc hành thiền.

Anumodanaa: Lời cầu chúc của nhà sư sau khi nhận lãnh của tín thí (tứ vật dụng).

Apaaya: Cảnh khổ. Có bốn cảnh khổ: súc sanh, ngạ quỉ, a-tu-la, địa ngục. Chúnh sinh ở những cõi này thiếu thiện nghiệp nên không có hạnh phúc.

Araha: Hoàn toàn trong sạch thanh tịnh, xứng đáng được người, trời và phạm thiên kính trọng. Ðây là ân đức đầu tiên trong mười ân đức của Phật.

Arahat hay Arahanta: A-la-hán hay Ứng Cúng, bậc thánh thứ tư. Là người hoàn toàn giác ngộ, diệt tận phiền não, không còn tâm bệnh. Sau khi chết không còn tái sinh nữa.

Ariyasaccani: Chân lý cao thượng. Xem thêm chữ attari ariyasaccani (Tứ Diệu Ðế)

Aasava: Hoặc lậu; ách nô lệ; trầm luân; trầm mịch hay dòng nước lũ. Bởi vì chúng trói buộc, nhận chìm và lôi cuốn chúng sinh trôi nổi trong sông mê bể khổ. Có bốn loại hoặc lậu:

1. Dục lậu (Kaamaasava): Ưa thích thụ hưởng những khoái cảm giác quan.

2. Hữu lậu (Bhavaasava): Khát vọng được tồn tại vĩnh viễn.

3. Kiến lậu (Di.t.thaasava): Quan kiến sai lầm về vũ trụ và nhân sinh. Có sáu mươi hai tà kiến hay quan kiến sai lầm nhưng có thể chia ra làm hai hai nhóm chính: thường kiến và đoạn kiến. Thường kiến, cho rằng bản ngã và thế giới trường tồn vĩnh cửu. Ðoạn kiến chủ trương bản ngã hoàn toàn hủy diệt sau khi thân hoại mạng chung.

4. Vô minh lậu (Avijjaasava): Không thấy rõ hay thấy sai lầm. (Xem chữ Avijjaa).

Aataapa: Rất nóng; Thiền có năng lực đốt cháy phiền não.

Avijjaa: Vô minh. Không thấy chân lý, nghĩa là không thấy được vô thường, khổ và vô ngã, và thấy sai lầm: cho rằng thế gian là trường tồn, an vui và có tự ngã.

Aayatana: Các xứ, gồm nội xứ và ngoại xứ. Nội xứ gồm: Mắt, tai, mũi, lưỡi, thân và tâm. Ngoại xứ gồm: Hình sắc, âm thanh, mùi, vị, vật xúc chạm và đối tượng của tâm.

[B]

Bhaavanaa: Tham thiền hay thiền, đốt cháy phiền não, gồm hai loại: thiền vắng lặng và thiền minh sát. (Xem chữ Samatha và Vipassanaa).

Bhikkhu: Tỳ khưu, tỳ kheo. Khất sĩ. Nam tu sĩ Phật giáo, giữ 227 giới, cạo đầu, mặc y vàng sống nhờ vào thực phẩm khất thực. Còn có nghĩa là những người cố gắng tu trì giới, định, huệ để giải thoát.

Bodhi: Giác ngộ, trí tuệ phát sinh vào lúc đạo tâm hiện khởi.

Bodhisatta: Bồ tát, người có hạnh nguyện trở thành một vị Phật toàn giác để có đủ khả năng cứu độ chúng sinh. Còn để chỉ Ðức Phật khi chưa giác ngộ.

Bojjha"nga: Yếu tố giác ngộ. Ðặc tính của tâm dẫn đến giác ngộ. Cũng là tuệ giác thấy rõ Tứ Diệu Ðế. (xem chữ sa"mbojja"nga)

Brahmaa: Phạm thiên. Tên của vị trời cao nhất. Tên của một cõi trời vô sắc, chỉ có tâm mà không có thân.

Brahmacariya: Phạm hạnh. Ðời sống thánh thiện, một đời sống cống hiến cho sự phát triển tinh thần. Ðời sống độc thân thánh thiện.

Brahma vihaara: Tứ vô lượng tâm: Từ, Bi, Hỉ, Xả.

Buddha: Phật. Ðấng giác ngộ. Danh từ được dùng để chỉ Thái tử Siddhattha Gotama, con của vua Suddhodana và hoàng hậu Maya. Vào năm hai mươi chín tuổi, Thái tử rời bỏ cung điện, xuất gia tu hành. Sau khi theo học với một số thầy và thực hành khổ hạnh trong sáu năm không hiệu quả, Thái tử tự tìm ra Trung Ðạo và giác ngộ do nỗ lực của chính mình. Trong bài pháp đầu tiên, Dhammacakka-pavatthana Sutta (Kinh Chuyển Pháp Luân), Ðức Phật đã dạy Bát Chánh đạo và Tứ Diệu Ðế.

Buddhaanussati: Niệm Ân Ðức Phật.

[C]

Caaga: Bố thí. dứt bỏ. Mong muốn loại trừ phiền não, cũng như có sự bố thí vật chất rộng rãi.

Cattaari ariyasaccaani: Tứ Thánh Ðế hay Tứ Diệu Ðế: (Bốn chân lý về sự khổ):

1. Chân lý về sự khổ (Dukkha): Sinh là khổ, già là khổ, đau là khổ, chết là khổ, xa lìa cái mình yêu thương là khổ, gần cái mình ghét là khổ, muốn không được là khổ...(sầu, bi, khổ, ưu, não là khổ)... ngũ uẩn thủ là khổ.

2. Chân lý về nguyên nhân của sự khổ (samudaya): Dục ái (kaamatanhaa), hữu ái (bhavatanhaa) và vô hữu ái (vibhavatanhaa).

3. Chân lý về sự diệt khổ (Nirodha): Hoàn toàn chấm dứt, là từ bỏ ái dục, tháo gỡ và giải thoát.

4. Chân lý về con đường dẫn đến nơi thoát khổ (magga): Ðó là Bát Chánh Ðạo.

Chanda: Dục: ý muốn làm

Citta: Tâm

Cittaa: Tên một vị tỳ khưu ni vào thời Ðức Phật. Tỳ khưu ni Cittaa đã chế ngự được sự đau yếu thể chất trầm trọng và sự yếu đuối, nỗ lực tinh tấn trở thành một vị A-la-hán.

Citta viveka: Tâm ẩn cư. Tâm ẩn cư khỏi mọi phiền não làm cản trở sự phát triển minh sát. Tương đương với liên tục chánh niệm, không để cho phiền não chế ngự.

[D]

Daana: Bố thí. Một trong mười Ba-la-mật (xem Paaramii). Ðây là pháp thực hành đầu tiên để loại trừ tâm tham ái.

Dasa kasina: Mười đề mục hành thiền: Tứ đại (đất, nước, gió, lửa), bốn màu sắc (xanh, vàng, đỏ, trắng), không gian, ánh sáng. Những đề mục hành thiền này giúp chế ngự tham ái.

Deva: (Nguyên nghĩa: Chúng sanh có ánh sáng). Các vị trời, có cơ thể vi tế nên mắt người không nhìn thấy được. Ðây là những chúng sanh sống trên các cõi trời, được an vui hạnh phúc hơn cõi người, nhưng khi hết tuổi thọ vẫn còn phải tái sanh trở lại chịu khổ trong sanh, già, đau, chết, tức là vẫn còn luân lưu trong vòng luân hồi.

Devadatta: Ðề-bà-đạt-đa. Một vị sư vào thời Ðức Phật, âm mưu chia rẽ giáo hội, và về sau nhiều lần muốn giết hại Ðức Phật.

Dhamma: Pháp, những lời dạy của Ðức Phật; bản chất của sự vật; luật thiên nhiên; chân lý.

Dhamma vicaya: Trạch pháp giác chi, một tâm sở thấy rõ bản chất các pháp, hay thấy rõ Niết bàn. Chi thứ hai trong Thất Giác Chi.

Dhuta"nga: Hạnh đầu đà, Thầy Tỳ khưu thực hành hạnh này để loại trừ phiền não. Người hành hạnh đầu đà giữ một số qui điều chặt chẽ, tri túc, từ bỏ, hạn chế các nhu cầu, chẳng hạn giữ hạnh: Chỉ dùng một bộ y gồm: y vai trái, y nội, y hai lớp; ăn ngày một bữa, sống trong rừng ....

Dosa: Sân hận, giận dữ, nóng giận. Tâm từ chối các đối tượng không vừa lòng; chẳng hạn, trong lúc hành thiền, tâm khó chịu khi cơ thể bị đau nhức. Sân hận là một trong ba phiền não chính khiến tâm chúng sinh mê mờ. Hai phiền não kia là tham lam và si mê.

Dukkha: Khổ, bất toại nguyện, đau khổ. Ðặc tính thứ hai của các pháp có điều kiện (pháp hữu vi). Ðây là kết quả của vô thường và tham ái. Khổ là chân lý đầu tiên trong Tứ Diệu Ðế, có ba loại khổ chính: khổ khổ, hành khổ và hoại khổ.

Dukkha lakkhanaa: Ðặc tính hay tướng của khổ nhờ đó mà thấy được khổ. Bị áp bức, bị đè nén bởi sự vô thường.

Dukkha-nupassanaa-~naana: Tuệ giác thấy được sự khổ. Trực giác được rằng không thể dựa vào ai hay cái gì cả, tất cả mọi đối tượng đều đáng sợ, đáng nhờm gớm, không nơi nào có thể nương nhờ hay ỷ lại vào vì tất cả đều bị hủy diệt, bị tan biến mau chóng.

[H]

Hiiri: Hỗ thẹn tội lỗi, cảm giác hỗ thẹn về những gì cần phải hỗ thẹn. Cảm giác hỗ thẹn khi làm hay nghĩ đến điều xấu xa, tội lỗi.

[I]

Issaa: Ganh tị. Không muốn nhìn thấy người khác thành công hay hạnh phúc.

[J]

Jetavana: Chùa Kỳ Viên. Một ngôi chùa gần thành Saavatthii (Xá-vệ) ở miền bắc Ấn Ðộ, nơi đức Phật thường dạy đạo.

Jhaana: Nhập định hay tầng thiền. Ðặc tính của tâm có khả năng dính chặt trên đối tượng và quan sát đối tượng, đốt cháy phiền não.

Jhaana sammaa di.t.thi: Chánh kiến trong các tầng thiền. Ðây là chánh kiến khởi sinh trong tám tầng thiền định, không phải trong thiền minh sát.

[K]

Kaccaayana: Ca-chiên-diên. Một trong những người học trò lớn của Ðức Phật, một vị A-la-hán, có khả năng diễn giải những bài pháp ngắn gọn của Ðức Phật. Nhiều bài Pháp của Ðức Phật chỉ vỏn vẹn có vài chữ.

Kalyaa.na mitta: Người bạn đức hạnh, người bạn tinh thần, thiện hữu.

Kaamacchanda: Dục lạc. Chướng ngại đầu tiên trong năm chướng ngại.

Kamma: Nghiệp. Hành động, lời nói hay tư tưởng cố ý. Nghiệp tích lũy trong quá khứ hay trong hiện tại sẽ trả quả trong hiện tại hay trong tương lai tùy theo tính chất của nghiệp.

Kammassakataa sammaa-dhi.t.thi: Chánh kiến thấy rõ chỉ có nghiệp mới thực sự là gia tài của chúng ta.

Kamma.t.thaana: Tham thiền.

Karu.naa: Lòng Bi mẫn. Tâm se lại trước sự đau khổ của chúng sinh khác. Lòng mong muốn loại bỏ những đau khổ của chúng sinh khác.

Kasina: Ðề mục hành thiền Kasina (Biến xứ). Có mười đề mục hành thiền Kasina: Ðất, nước, lửa, gió, xanh, vàng, đỏ, trắng, ánh sáng, "khoảng không" có giới hạn.

Kaaya: Thân thể, hình dáng.

Kaaya viveka: Thân ẩn cư, điều kiện đầu tiên giúp cho việc hành thiền tốt đẹp. Thái độ không dính mắc vào lục trần: sắc, thinh, hương, vị, xúc và pháp. Cũng có nghĩa là thân xa lánh các nơi ồn ào náo nhiệt. Hằng ngày đến nơi yên tịnh vắng lặng để hành thiền.

Khandaa: Uẩn, nhóm, tập hợp. Thân người là tập hợp của năm uẩn: Sắc (ruupa), thọ (vedanaa), tưởng (sa~n~naa), hành (sa"nkhaara), thức (vi~n~naana).

Khema: Tịnh an. An ninh, an toàn. Một trong những đặc tính của Niết bàn, trái hẳn với sự an toàn có điều kiện của thế gian.

Kilesaa: Phiền não, những yếu tố làm cho tâm ô nhiễm. Phiền não có thể khởi dậy ngay cả khi các điều kiện của chúng đã được loại trừ.

Kilesaa parinibbaana: Hoàn toàn loại trừ phiền não.

Kodha: Sân hận, nóng nảy, "tâm gai góc". Sân hận và những tâm sở đi kèm với sân hận.

Kusala: Thiện, tốt.

Kusiita: Người lười biếng.

[L]

Lakkha.naa: Ðặc tính.

Lobha: Tham. Tâm nắm giữ vật ưa thích.

Lokiya: Thế tục.

Lokuttara: Siêu thế. Ðây là từ để chỉ bốn đạo, bốn quả và Niết bàn.

[M]

Macchariya: Bủn xỉn. Không muốn thấy người khác hạnh phúc như mình.

Magga: Ðạo. Danh từ để chỉ giây phút giác ngộ, khi mọi phiền não đều được loại trừ. Tâm đầu tiên của Niết bàn.

Mahaakassapa: Ma-ha (Ðại) Ca-diếp. Một trong những vị học trò đầu tiên của Ðức Phật. Ngài là vị tỳ khưu đệ nhất đầu đà, chủ tọa kỳ kết tập Tam Tạng lần đầu tiên sau khi Ðức Phật niết bàn ba tháng.

Mahaamoggallaana: Ðại Mộc Kiền Liên. Một trong hai Ðại Ðệ Tử của Ðức Phật, có thần thông bậc nhất.

Mahaapajaapati Gotamii: Người dì đồng thời cũng là mẹ kế của Thái Tử Siddhatta. Vị nữ tỳ khưu đầu tiên, sáng lập Tỳ khưu ni đoàn. Vị thánh đệ nhất về sự chứng đắc.

Mahaayaana: Ðại thừa. Sau khi hoàng đế Asoka cố gắng hợp nhất Tăng Chúng vào thế kỷ thứ ba trước Công nguyên, một số tông phái tự động phát triển các học phái của riêng mình. Một số quan điểm của Ðại thừa khác hẳn giáo lý thời nguyên thủy, chẳng hạn như quan điểm về Bodhisattva (Bồ tát): Bồ tát từ khước Niết bàn để có thể tiếp tục sống trong Tam Giới cứu độ chúng sinh. Trong khi đó Phật giáo Nguyên thủy dựa vào lời dạy cuối cùng của Ðức Phật trước khi nhập diệt, khuyến khích mọi người hãy "tự nổ lực để cứu độ chính mình" (Xem kinh Mahaaparinibbaana Sutta, Ðại Bát Niết Bàn, Trường Bộ). Ðại Thừa thêm vào nhiều kinh điển mà thời Phật Giáo Nguyên Thủy không có. Phật giáo Ðại thừa được truyền bá vào Trung Á do các thương buôn và các nhà sư thời vua Kushan ở Ấn Ðộ trong suốt hai thế kỷ đầu tiên sau Công nguyên và dần dần lan tràn sang Tây tạng, Trung hoa, Siberia, Triều tiên, Nhật bản và Việt nam. Từ thế kỷ thứ tám đến thế kỷ thứ mười ba được truyền sang Cam Bốt, Java, Sumatra và Mã lai.

Maana: Mạn. Có ba loại mạn: Cho mình hơn người, cho mình bằng người, cho mình thua người.

Maara: Ma vương. Theo nguyên ngữ Paa.li, Maara được rút ra từ một từ gốc có nghĩa là "sự chết". Nhân cách hóa sức mạnh của si mê và ái dục. Si mê và ái dục hủy hoại đức hạnh và mạng sống chúng sinh, là chủ tể của mọi cảnh giới có điều kiện.

Maatikamaataa: Một tín nữ vào thời Ðức Phật, hỗ trợ chư tăng hành thiền. Trong lúc lo nấu nướng cho chư tăng bà luôn luôn chú tâm chánh niệm vào việc làm, chẳng bao lâu sau bà đắc quả.

Mettaa: Từ ái, tâm Từ. Mong cầu tất cả chúng sinh có đầy đủ sức khỏe, thân tâm an lạc.

Middha: Buồn ngủ. Tâm trở nên tiêu cực, thụ động khi buồn ngủ có mặt.

Moha: Si mê. Tâm không đủ khả năng nhận biết những điều xảy ra, đặc biệt là các cảm giác vô ký. Một trong ba Phiền não chính (tham, sân, si) làm tâm chúng sinh mê mờ, đen tối.

Muditaa: Hỉ. Vui mừng trước sự thành công, hạnh phúc của kẽ khác.

[N]

Naama: Danh hay tâm. Tâm, theo nguyên nghĩa, là cái hướng đến đối tượng hay cái làm cho những cái khác hướng đế chúng. Ðây là một từ để chỉ mọi hiện tượng của tâm.

Namuci: Một tên khác của Maara.

Nekkhamma sukha: Hạnh phúc của sự khước từ, hạnh phúc của sự xuất gia. Hạnh phúc, an lạc và thoải mái đến từ sự xa lìa dục lạc ngũ trần, xa lìa những phiền não do dục lạc thú ngũ trần đem lại.

Nibbaana: Niết Bàn. Không điều kiện, hoàn toàn không có phiền não vì không phải là thân hay tâm.

Nikanti ta.nhaa: Tham luyến vào những lạc thú do thiền đem lại. Ðây là một loại phiền não rất vi tế, mong manh như mạng nhện nhưng làm cản trở bánh xe trí tuệ.

Nimita: "Tướng" hay hình ảnh trong tâm xuất hiện lúc hành thiền, cho thấy khả năng định tâm cao.

Nirodha: Diệt, chấm dứt.

Nirodha samaapatti: Diệt Thọ Tưởng Ðịnh. Ðạt được sự diệt. Ðây là loại định tâm mà chỉ có vị A-la-hán hay A-na-hàm mới có thể vào được.

Niivarana: Chướng ngại, Triền cái. Có năm chướng ngại trên đường giải thoát, giác ngộ: Tham ái, sân hận, giao động hối hận, dã dượi buồn ngủ và hoài nghi.

[O]

Ottappa: Ghê sợ tội lỗi. Không muốn làm điều ác vì sợ hậu quả tai hại của nó; đây là thái độ của người trí.

[P]

Pabbajita: Xuất gia hay từ bỏ. Người từ bỏ đờ sống thế tục để diệt trừ phiền não.

Pacceka Buddha: Ðộc Giác Phật. Tự mình giác ngộ, nhưng sau khi giác ngộ không thể giảng dạy cho người khác.

Paccakkha-~naa.na: Tri giác tuệ. Tri giác do kinh nghiệm trực tiếp. Tuệ giác trực tiếp. Ðồng nghĩa với chữ Vipassanaa.

Paa.li: Ngôn ngữ dùng để ghi kinh điển Phật giáo, gần với tiếng Magadhii (Ma-kiệt-đà). Ðây là ngôn ngữ mà Ðức Phật và các đệ tử của Ngài dùng để giảng dạy và nói chuyện hằng ngày.

Paamojja, paamujja: Khinh hỉ hay thiểu hỉ. Loại hỉ đầu tiên trong năm loại hỉ.

Pancendriya: Ngũ căn. Một từ về thiền để chỉ năm tâm sở: Tín, Tấn, Niệm, Ðịnh, Huệ.

Pa~n~naa: Trí tuệ. Trí tuệ trực giác về chân lý tối thượng.

Paramattha dhamma: Thực tại tuyệt đối. Chân đế. Ðối tượng được nhận biết một cách trực tiếp không qua khái niệm. Có ba loại chân đế: hiện tượng vật chất, hiện tượng tâm và Niết bàn.

Paramatha sacca: Chân lý tuyệt đối. Cùng nghĩa với paramattha dhamma. (phản nghĩa với sammuti sacca).

Paaramii: Ba-la-mật. Hoàn hảo. Sức mạnh thanh tịnh nội tâm được phát triển và tích lũy qua nhiều đời. Có mười ba-la-mật: daana (bố thí), siila (trì giới), nekkhama (xuất gia hay khước từ), pa~n~naa (trí tuệ), viiriya (tinh tấn), khanti (nhẩn nhục), sacca (chân thật), adhi.t.thaana (quyết định), mettaa (tâm từ) và upekkhaa (tâm xả).

Parinibbaana: Bát Niết Bàn, Vô Dư Niết Bàn. Một vị Phật hay A-la-hán khi còn sống thì có Hữu Dư Niết Bàn, lúc rời bỏ thân thể này thì gọi là Vô Dư Niết Bàn.

Parisuddhi sukha: Tịnh lạc. Hạnh phúc an lạc không trộn lẫn với phiền não. Niết bàn.

Passaddhi : Thư thái. Chi thứ năm trong thất giác chi.

Paticca samuppaada: Thập nhị nhân duyên.

Paatimokkha: Giới bổn, Ba-la-đề-mộc-xoa. Giới luật được ghi trong tạng Luật (227 giới cho Tỳ khưu và 311 giới cho Tỳ khưu ni), tạng đầu tiên trong Tam Tạng Paa.li. Chư Tăng Ni mỗi tháng phải tụng giới bổn hai lần vào ngày mười bốn và ba mươi mỗi tháng

Peta: Ngạ quỉ. Quỉ đói. Loại quỉ không có hạnh phúc.

Phala: Quả. Tâm xảy ra tiếp theo đạo tâm, tiếp tục thấy Niết Bàn, và trong khi đó thì phiền não bị loại trừ.

Phassa: Xúc, một tâm sở phát sanh khi tâm tiếp xúc với đối tượng.

Pin.dapaata: Trì bình hay khất thực: chư tăng ôm bát nhận cơm cúng dường của bá tánh.

Piiti: Hỉ. Nhờ tâm trong sáng thanh tịnh nên thân và tâm có cảm giác nhẹ nhàng thích thú.

Puthujjana: Thế tục, phàm nhân.

[R]

Raaga: Dục ái. Tham ái.

Ruupa: Sắc, vật chất.

[S]

Saddhaa: Ðức tin, Tín.

Sahagata: Ði kèm với. Phối hợp với.

Sakadaagaami: Tư-Ðà-Hàm. Nhất Lai. Tham ái và sân hận của vị có quả thánh thứ hai đã yếu kém nên chỉ còn tái sinh một lần.

Samatha bhaavanaa: Thiền vắng lặng. Thiền An Chỉ. Hành thiền theo bốn mươi đề mục nhằm mục đích đạt được tâm vắng lặng. Bình an do chế ngự được một số phiền não và chướng ngại.

Samaadhi: Ðịnh. Trạng thái của tâm trụ trên một đối tượng duy nhất. Có ba loại Ðịnh: chuẩn bị (Parikamma), cận định (upacaara) và định (jhaana hay appanaa). Chi thứ sáu trong Thất Giác Chi.

Saama.nera: Sa di.

Saama.nerii: Sa di ni.

Samatha jhaana: Nhập Ðịnh. Tâm hoàn toàn an trú trong một đề mục duy nhất. ở trong tình trạng hoàn toàn an tịnh, tĩnh lặng, tâm thấm nhập vào đề mục.

Sa"mbojjha"nga: Thất giác chi. Bảy yếu tố giác ngộ. Bảy nhân sinh quả bồ đề gồm: Chánh niệm (sati), Trạch pháp (dhamma vicaya), tinh tấn (viiriya), hỉ (piiti), Thư thái (passaddhi), định (samaadhi) và xả (upekkhaa).

Sammaa-di.t.thi: Chánh kiến. Kiến thức chân chánh.

Sammaa-kammanta: Chánh nghiệp. Hành động chân chánh: Không sát sanh, không trộm cắp, không tà hạnh.

Sammaa-sambuddha: Tam-miệu tam-bồ-đề. Chánh đẳng chánh giác, tự mình ngộ lấy không thầy chỉ dạy.

Sammasana-~naa.na: Tư duy trí. Tuệ thấy rõ: vô thường, khổ não, vô ngã. Ðạt tuệ này, thiền sinh thấy rõ sự tan rã, sự biến mất một cách nhanh chóng của đối tượng. Với sự thấy rõ này, thiền sinh kinh nghiệm trực tiếp rằng tất cả mọi vật đều vô thường, bất toại nguyện và không có tự ngã. Ðược gọi là "liễu tri" vì thiền sinh tự mình thấy rõ chân lý căn bản.

Sammaa vaacaa: Chánh ngữ. Lời nói chân chánh: lời nói thành thật, lời nói đem lại sự đoàn kết, lời nói dịu dàng, lời nói hữu ích.

Sa"mpajja~n~na: Giác tỉnh. Biết mình. Hiểu biết sáng suốt.

Samsaara: Vòng luân hồi. Vòng tham ái và đau khổ do không hiểu biết chân lý

Samudaya: Khởi sinh.

Samudaya dhamma: Pháp duyên sinh.

Samutti sacca: Tục đế. Sự thật thế tình. Ngược với chân đế: sự thật tuyệt đối. Tục đế dính mắc quan niệm, vào danh từ như cho rằng có tôi, anh, chị, ghế, bàn, sông, núi ... Chân đế nhìn đúng bản chất của sự vật nên không có tôi, anh, chị, ghế, bàn, sông, núi ... mà chỉ có vật chất và tinh thần thuần túy hay danh và sắc hoặc thân và tâm

Sangha: Tăng già. Chúng. Cộng đồng tu sĩ Phật giáo gồm những nhà sư ăn mặc theo Phật, tu trì Giới (227 giới), Ðịnh, Huệ.

Sa"nkhaara: Hành. Trong thập nhị nhân duyên thì hành có nghĩa là tác ý. Trong ngũ uẩn thì hành chỉ cho năm mươi tâm sở. Hành còn có nghĩa là danh sắc hay các pháp có điều kiện, chẳng hạn như câu: Các pháp hành đều vô thường, hãy tinh tấn, chớ phóng dật. Chữ hành ở đây có nghĩa là các pháp có điều kiện hay danh sắc

Sa"nkhaara paramattha dhamma: Chân lý tuyệt đối về các pháp có điều kiện. Hiện tượng danh sắc hay thân tâm được trực tiếp thấy rõ, không xuyên qua tư duy hay khái niệm.

Sa"nkhaarupekkhaa~naa.na: Tuệ xả. Có tâm xả thọ đối với tất cả mọi pháp (duyên sinh). Một trong những tuệ giác cao nhất trong thiền minh sát. Một trạng thái quân bình nội tâm tinh tế không bị ảnh hưởng bởi các cảm thọ vui khổ.

Sa~n~naa: Tưởng. Ttri giác, ý niệm, quan kiến, trí nhớ.

Santi sukha: Tịnh lạc. Hạnh phúc tịch tịnh. Một từ để chỉ kinh nghiệm Niết bàn.

Saariputta: Xá-lợi-phất. Một trong hai đại đệ tử của Phật, có trí tuệ bậc nhất.

Sati: Chánh niệm. Ghi nhớ đúng đắn. Chi thứ nhất trong thất giác chi.

Satipa.t.thaana: Tứ niệm xứ. Bốn căn bản của chánh niệm: niệm thân, niệm thọ, niệm tâm và niệm pháp.

Satipa.t.thaana Sutta: Kinh Tứ niệm xứ. Một bài kinh trong đó Ðức Phật chỉ dạy cách thực hành chánh niệm.

Sayadaw: Ðại sư. Một danh từ của người Miến Ðiện để tôn xưng một thiền sư hay một vị trụ trì.

Siila: Giới. Ðức hạnh.

Siilashin: Tu nữ Miến Ðiện, giữ tám hay mười giới, Mặc y phục vàng, hồng hay nâu.

Sona Therii: Tên một vị tỳ khưu ni. Bị con cái ruồng bỏ, bà Sona vào chùa tu và đắc quả.

Sotaapanna: Tu-đà-huờn, Nhập lưu. Ðắc quả thánh thứ nhất, kinh nghiệm Niết Bàn lần đầu tiên, dứt trừ ba dây trói buộc: thân kiến, hoài nghi, giới cấm thủ. Vì các phiền não đã yếu nên vị Tu-đà-huờn không bị tái sinh vào bốn cõi dữ. Còn gọi là Thất Lai vì vị Tu-đà-huờn chỉ còn tái sinh tối đa bốn kiếp.

Subhadda: Một tu sĩ ngoại đạo trở thành người học trò cuối cùng của Ðức Phật. Subhadda trở thành một vị tỳ kheo Phật giáo trước khi Phật nhập Niết Bàn độ vài giờ đồng hồ.

Sukha: Lạc, hoan hỉ, cảm giác vui vẻ. Chi thứ tư trong tầng thiền định thứ nhất.

Sumedha: tên một vị ẩn sĩ giữ hạnh bồ tát để trở thành một vị Phật toàn giác. Ðây là vị bồ tát tiền thân Phật Thích Ca.

Sutta: Kinh. Ghi lại những lời giảng của Ðức Phật. Tạng thứ hai trong Tam Tạng Paa.li.

[T]

Ta.nhaa: Ái dục, tham ái, lòng tham muốn dẫn đến tái sinh.

Theravaada: Nguyên ngữ là lời dạy của những vị trưởng lão. Trưởng lão bộ, Bảo thủ bộ, Thượng tọa bộ hay Phật giáo Nguyên thủy. Một tông phái duy nhất trong số mười tám tông phái còn lại sau khi Phật Niết bàn. Các vị trưởng lão tụng đọc lại tất cả những lời dạy của Ðức Phật vào kỳ kết tập Tam Tạng lần thứ nhất, ba tháng sau khi Phật Niết bàn. Những lời dạy này được nhóm trưởng lão bảo thủ lưu giữ cho đến ngày nay. Phật Giáo Nguyên Thủy được duy trì và phổ biến tại các xứ Miến Ðiện, Thái Lan, Kampuchia, Lào, và Tích Lan.

Tatra majjhattataa: Quân bình nội tâm. Một khía cạnh của tâm xả.

Taavatimsa: Cõi trời Ðao Lợi còn gọi là cõi trời Tam thập tam thiên: cõi trời của ba mươi ba vị trời. Ðây là cõi trời mà Ðức Phật thuyết vi diệu pháp cho Phật mẫu nghe. Hoàng hậu Maya sau khi chết tái sinh vào cõi trời này.

Thera: Trưởng lão tăng. Thường được dùng để trước tên những vị Tăng cao hạ để bày tỏ lòng kính trọng.

Therii: Trưởng lão ni. Thường được dùng để trước tên những vị Ni cao hạ để bày tỏ lòng kính trọng.

Thina: Dã dượi.

Thina middha: Dã dượi buồn ngủ. Dã dượi và buồn ngủ thường đi đôi với nhau. Dã dượi là tâm co rút lại như lông gà đặt gần lửa thì bị teo lại. Buồn ngủ là một tâm thụ động đi theo dã dượi. Thiina middha là chướng ngại thứ tư trong năm chướng ngại, là đạo binh thứ năm trong mười đạo binh ma.

Tipi.taka: Tam tạng kinh. Gồm ba tạng: Luật (Vinaya) giới điều, (những qui luật mà tăng Ni phải hành trì), Kinh (Sutta) và Vi diệu pháp (Abhidhamma)

Tisara.na: Tam qui. Qui y Phật, qui y Pháp, qui y Tăng.

[U]

Uddhacca kukkucca: Trạo hối. Bất an giao động và hối hận. Chướng ngại thứ tư trong năm chướng ngại

Uddhata: Bất an, nguyên nghĩa là giao động.

Udaka Raamaputta: Một thiền sư nổi tiếng thời Ðức Phật, một trong hai vị thầy của Bồ tát Sĩ Ðạt Ta.

Upaadaana: Chấp thủ. Tâm tham ái dính chặt vào đối tượng không buông rời

Upasama: Bình an, tĩnh lặng

Upekkhaa: Xả. Quân bình năng lực. Ðặc tính của tâm thăng bằng không nghiêng về một thái cực nào. Chi thứ bảy trong thất giác chi.

[V]

Vaya dhamma: Pháp diệt.

Vedanaa: Thọ hay cảm thọ.

Vicaara: Tứ hay Sát. Một khía cạnh của sự định tâm bao gồm tâm "chà xát" trên đối tượng. Yếu tố thứ hai trong tầng thiền định đầu tiên.

Vicikicchaa: Hoài nghi. Tâm mệt mỏi vì phân vân không quyết và ức đoán. Chướng ngại thứ năm trong năm chướng ngại. Ðạo binh ma thứ bảy trong mười đạo binh ma.

Vikkhambhana viveka: Tị phiền não ẩn cư. Trạng thái phiền não bị yếu kém trong một thời gian. Ðây là kết quả của thân ẩn cư và tâm ẩn cư.

Vinaya: Luật (xem Paa.timokkha)

Vi~n~naa.na: Thức.

Vipaaka: Quả của nghiệp. Những điều kiện sinh khởi do hành động quá khứ

Vipassanaa: Thiền minh sát. Nguyên nghĩa: 'thấy bằng nhiều cách'. Năng lực quán sát đối tượng thân tâm qua ánh sáng của vô thường, khổ não và vô ngã.

Vipassanaa jhaana: 1) Tiếp tục chú tâm vào bản chất thật sự (chân đế) của sự vật không xuyên qua sự suy nghĩ hay khái niệm. 2) Trụ tâm vào các đề mục thay đổi, nhưng vẫn chú tâm khắn khít vào đặc tính vô thường, khổ và vô ngã.

Vipassanaa kilesa: Minh sát phiền não. Ðây là những loại phiền não khởi sinh lúc thiền sinh đạt đến tuệ giác thấy rõ sự sinh diệt mau chóng của các hiện tượng. Hỉ lạc phát sinh vào lúc này. Minh sát phiền não bao gồm sự nắm giữ những kinh nghiệm hỉ lạc do việc hành thiền đem lại mà không biết rằng mình đang dính mắc vào chúng.

Viiraana"m bhaavo: Dũng cảm. Ðặc tính của một anh hùng. Ðây là từ để chỉ sự dũng cảm tinh tấn trong việc hành thiền.

Virati: Sự thu thúc, sự kiêng cử.

Viriya: Tinh tấn. Năng lực hay sự tinh tấn liên tục hướng tâm đến đối tượng. Ðược rút ra từ chữ anh hùng. Chi thứ ba trong thất giác chi.

Visuddhi Magga: Thanh Tịnh Ðạo. Một cuốn sách viết về Thiền do Ngài Buddhaghosa soạn vào thế kỷ thứ tư sau Công nguyên.

Vitakka: Tầm: Một khía cạnh của định tâm, tâm hướng về đối tượng, dính trên đối tượng và đặt trên đối tượng. Chi thứ nhất của tầng thiền định đầu tiên.

Viveka: ẩn cư. Một từ chỉ trạng thái an tịnh tĩnh lặng, xuắt hiện khi tâm được an trú và bảo vệ không bị phiên não quấy nhiễu.

Vivekaja piiti sukha: ẩn cư hỉ lạc. Hỉ lạc, hạnh phúc do sự ẩn cư đem lại. Một từ để chỉ hai chi thiền thứ ba và thứ tư của tầng thiền định đầu tiên, được xem như phối hợp chung với nhau.

Vyaapaada: Sân hận. Chướng ngại thứ hai trong năm chướng ngại.

[Y]

Yogi: Thiền sinh.''')
  text = st.text_area('Enter text in English:', '''''')
  submitted = st.form_submit_button('Submit')
  
  if submitted:
    if not text:
      st.warning('Please enter your english text first', icon='⚠')
    else:
      st.info(generate_response(text, dictionary))
