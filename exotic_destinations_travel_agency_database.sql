CREATE DATABASE  IF NOT EXISTS `exotic_destinations_travel_agency` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `exotic_destinations_travel_agency`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: exotic_destinations_travel_agency
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accommodations`
--

DROP TABLE IF EXISTS `accommodations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accommodations` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `type` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accommodation_uc` (`name`,`type`,`description`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accommodations`
--

LOCK TABLES `accommodations` WRITE;
/*!40000 ALTER TABLE `accommodations` DISABLE KEYS */;
INSERT INTO `accommodations` VALUES ('fde507e0-fcc3-403b-9c64-1ae448cfa7a7','Guesthouse','guesthouse','Guest house is an accommodation facility that has less spacious double and triple rooms with their own bathroom.'),('a991864b-fefc-4ec2-8f71-687b5caa3e8e','Hotel 3*','hotel','Hotel with three stars according to local categorization, accommodation facility typical for Africa. The hotel has double and triple rooms with private bathroom. The rooms have air conditioning and television.');
/*!40000 ALTER TABLE `accommodations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arrangements`
--

DROP TABLE IF EXISTS `arrangements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `arrangements` (
  `id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `code` varchar(10) NOT NULL,
  `date_of_departure` date NOT NULL,
  `date_of_arrival` date NOT NULL,
  `duration` int NOT NULL,
  `description` varchar(1000) NOT NULL,
  `air_route_to_the_destination` varchar(1000) NOT NULL,
  `price` float NOT NULL,
  `demandingness` int NOT NULL,
  `availability` tinyint(1) NOT NULL,
  `included_in_price` varchar(1000) NOT NULL,
  `not_included_in_price` varchar(1000) NOT NULL,
  `state_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `arrangements_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arrangements`
--

LOCK TABLES `arrangements` WRITE;
/*!40000 ALTER TABLE `arrangements` DISABLE KEYS */;
INSERT INTO `arrangements` VALUES ('5392665e-f8a2-49b3-a208-6bb79e8b1603','Zanzibar','zbr','2023-06-21','2023-07-01',11,'Go with our tribe on a ten-day conquest of magical Zanzibar.This faraway destination, ideal for traveling with children, will leave you breathless. Dive into a real tropical paradise, get to know Stone Town, drink a cocktail at the famous The Rock, visit a spice farm and relax on the most beautiful beaches of Tanzania and Zanzibar.During the trip to Zanzibar, we walk and explore the streets of Stone Town, which represent a real small labyrinth: food, taste, color, music, smiling people, African rhythm, market stalls, centuries-old history.','Belgrade->Istanbul->Paje->Istanbul->Belgrade',1150,1,1,'Accommodation, Airline ticket with all taxes on the route Belgrade - Zanzibar, in economy class with a transfer with 30 kg of checked and 8 kg of hand luggage,Transfer from the airport to the accommodation,Transfer from the accommodation to the airport,Airline ticket with all taxes on the route Zanzibar - Belgrade, in economy class with a transfer with 30 kg of checked and 8 kg of hand luggage, 8 × Continental breakfast','International health insurance (can be taken at the agency),Individual expenses incurred during the duration of the arrangement,Optional excursions and tickets for cultural and historical monuments,Tanzania visa ($50), at the border,Surcharge for fuel tax increase','5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('8f02596b-2170-423f-a6d8-834eb846a8d5','Maldives','mld','2023-03-06','2023-03-15',10,'Winter in the Maldives will leave you breathless. On this trip, we will visit one of the 200 inhabited islands and enjoy white beaches and incredibly blue and clear water. Whether you\'re going on a honeymoon or a family vacation, everything in the Maldives is about enjoyment!','Belgrade->Dubai->Male->Maafushi->Male->Dubai->Belgrade',1290,1,1,'Accommodation, Airline ticket with all taxes on the Belgrade-Male route, in economy class with a transfer with 20 kg of checked and 7 kg of hand luggage,Transfer from the airport to the accommodation,Transfer by speedboat from the accommodation to the airport,Airline ticket with all taxes on the Male-Belgrade route, in economy class with a transfer with 20 kg of checked and 7 kg of hand luggage, 1 × Dinner (for half and full board services), 7 × Continental breakfast, 6 × Lunch (full board service pension), 6 × Dinner (half board and full board service), 13 tours: diving with sharks, going to Fulidhoo Island and hanging out with stingrays, going to the sandbank (sandbank), watching dolphins, going to the sandbank with a campfire, snorkeling with manta rays, snorkeling with turtles, snorkeling at Biyadhoo coral reef, hotel rooftop tea party, tour of the capital of Male, kayaking / paddleboarding, snorkeling at the local coral reef, romantic dinner on the beach','International health insurance (can be taken at the agency),Individual expenses incurred during the duration of the arrangement,Optional excursions and tickets for cultural and historical monuments,Surcharge for a single room,Surcharge for fuel tax increase,Surcharge for a room with a sea view in the amount of 70 EUR per person','5d92b93e-82c4-4332-8a14-d158f21ee488'),('93e92098-446c-410b-ba96-66d43b66fa2a','Morroco promo','mrc','2023-09-07','2023-09-15',9,'On this trip to Morocco, we will have the opportunity to try a variety of Moroccan food, drink tea with Berbers, go on a trip to the capital Rabat and Casablanca, swim in the cool waters of Ouzoud Falls and take pictures with monkeys. The rich stalls in Marrakesh will give us the opportunity to buy various souvenirs: sweets, teas, jewelry, leather handbags, scarves and to stroll through the main square of Djema el Fna. Excursions to the Agafay desert, Essaouira and Ourika will complete your trip to Morocco and leave a special impression on you.','Belgrade->Istanbul->Marrakesh->Istanbul->Belgrade',950,2,1,'Accommodation, plane ticket with all taxes on the Belgrade-Marrakech route, in economy class with a transfer with 30 kg of checked and 7 kg of hand luggage,Transfer from the airport to the accommodation,Transfer from the accommodation to the airport,Airline ticket with all taxes on the Marrakesh-Belgrade route, in economy class with a transfer with 30 kg of checked and 7 kg of hand luggage, 7 × Continental breakfast','International health insurance (can be taken at the agency),Individual expenses incurred during the duration of the arrangement,Optional excursions and tickets for cultural and historical monuments,International health insurance (can be taken at the agency),Visa for Morocco (4950 rsd + 500 rsd visa service)','4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('fac19cb1-8991-4a9d-96fe-3f5250dc0c34','Mauritius','mrt','2023-03-10','2023-03-22',13,'Unspoiled nature, sparkling blue sea, colorful flowers and fine white sand... welcome to the heavenly world! All this can be seen in tourist pictures and photos, however, Mauritius is the right choice for all those who want recreation and sports. This is a destination that will satisfy even the most demanding adventurer because it offers superb hiking, kite surfing and diving. A massive coral reef surrounds the entire island and is a real delight for experienced divers. Hospitable Mauritius offers not only beautiful weather and fantastic beaches, but a cultural identity worth exploring.','Belgrade->Istanbul->Trou aux Biches->Istanbul->Belgrade',1490,1,1,'Accommodation, Airline ticket with all taxes on the route Belgrade - Mauritius, in economy class with a transfer with 2 x 23 kg checked and 8 kg hand luggage,Transfer from the airport to the accommodation,Transfer from the accommodation to the airport,Airline ticket with all taxes on the route Mauritius - Belgrade, in economy class with a transfer with 2 x 23 kg checked and 8 kg hand luggage, 1 × Dinner, 6 × Half board (breakfast and dinner), 1 × Breakfast','International health insurance (can be taken at the agency),Individual expenses incurred during the duration of the arrangement,Optional excursions and tickets for cultural and historical monuments,Surcharge for a single room,Surcharge for fuel tax increase','bb4e3ee9-8b25-4244-9341-1eff83b3d4a5');
/*!40000 ALTER TABLE `arrangements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `excursions`
--

DROP TABLE IF EXISTS `excursions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `excursions` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` float NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oe_uc` (`name`,`price`,`description`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `excursions`
--

LOCK TABLES `excursions` WRITE;
/*!40000 ALTER TABLE `excursions` DISABLE KEYS */;
INSERT INTO `excursions` VALUES ('2451c06a-b2ec-4e9c-9ad0-cecb507e9e95','Blue safari',60,'On the Blue Safari excursion, we go on an adventure along the endless blue of Zanzibar\'s beaches and sandbanks known for their crystal white fine sand. Above us is a blue sky dotted with traveling clouds, and below us is the Indian Ocean in all its majesty. We sail in traditional dhow boats that have been used by Zanzibari for hundreds of years and enjoy the sparkling turquoise water, tropical sun, exotic fruits and magical shores of the islands of the Zanzibar archipelago.'),('1098e121-af87-4d14-8d41-cc30c11172ae','Spice farm, Pađe village and dolphin watching',55,'Zanzibar is also known in the world as the island of spices. During the colonization of this island, the Arabs, famous traders and sailors, brought various spices from many parts of the world. Zanzibar\'s climate proved perfect for a huge number of them and today there are several spice farms on this magical island. We will visit the largest farm and get to know the diversity of spices that Zanzibari use in their cuisine.'),('2e56a1bd-7403-417b-9da6-637c9ea036bd','Stone town, Prison Island, Nakupenda',50,'We leave for the trip in the morning. We will visit the Old Fortress, which is also called the Portuguese Fortress, because its foundations were struck by the Portuguese. Right next to the fortress is the House of Miracles, one of the main symbols of Zanzibar, the former ceremonial palace of the third Sultan of Zanzibar, Sultan Baragash, which was the first in East Africa to have electricity, water supply and an electric elevator. We will have the opportunity to see the palace of the last sultan');
/*!40000 ALTER TABLE `excursions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plan_and_program_per_day`
--

DROP TABLE IF EXISTS `plan_and_program_per_day`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plan_and_program_per_day` (
  `id` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `food` varchar(500) NOT NULL,
  `excursion_id` varchar(50) DEFAULT NULL,
  `accommodation_id` varchar(50) DEFAULT NULL,
  `arrangement_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `p_and_p_uc` (`title`,`arrangement_id`),
  KEY `excursion_id` (`excursion_id`),
  KEY `accommodation_id` (`accommodation_id`),
  KEY `arrangement_id` (`arrangement_id`),
  CONSTRAINT `plan_and_program_per_day_ibfk_1` FOREIGN KEY (`excursion_id`) REFERENCES `excursions` (`id`),
  CONSTRAINT `plan_and_program_per_day_ibfk_2` FOREIGN KEY (`accommodation_id`) REFERENCES `accommodations` (`id`),
  CONSTRAINT `plan_and_program_per_day_ibfk_3` FOREIGN KEY (`arrangement_id`) REFERENCES `arrangements` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_and_program_per_day`
--

LOCK TABLES `plan_and_program_per_day` WRITE;
/*!40000 ALTER TABLE `plan_and_program_per_day` DISABLE KEYS */;
/*!40000 ALTER TABLE `plan_and_program_per_day` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `state_informations`
--

DROP TABLE IF EXISTS `state_informations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `state_informations` (
  `id` varchar(50) NOT NULL,
  `info_title` varchar(500) NOT NULL,
  `details` varchar(2000) NOT NULL,
  `is_mandatory` tinyint(1) DEFAULT NULL,
  `state_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `info_uc` (`info_title`,`state_id`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `state_informations_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state_informations`
--

LOCK TABLES `state_informations` WRITE;
/*!40000 ALTER TABLE `state_informations` DISABLE KEYS */;
INSERT INTO `state_informations` VALUES ('05f4c838-155b-4a2e-8bef-af5722a6c448','food','Drink only bottled water and brush your teeth with it, avoid ice, and as far as food is concerned, you can eat whatever you want, only when you eat fruits and vegetables be sure to wash them with bottled water or peel them. Food in Zanzibar is based on rice, spices like curry, nutmeg combined with meat, fish, octopus and lobsters.The traditional diet includes chicken, beef (in the form of barbecue or stew), rice, vegetables and fruits, and in Zanzibar, seafood and fish. Street food is not recommended (primarily because this is not an area with a tradition of street food). Meal prices in Zanzibar can vary, and the average price in restaurants is $15-18. Breakfast prices are usually slightly cheaper than lunch or dinner.',NULL,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('0b906137-f6bf-4023-9071-a98b1d1fdecc','other notes','Starting from 01.06.2019. all travelers traveling to Tanzania must not carry any plastic bags with them, as heavy fines apply for breaking this rule from this date. Using, manufacturing or importing plastic bags is illegal. It is advised that all visitors avoid packing in any plastic bags, both in checked and hand luggage. Products purchased at the airport and packed in plastic bags must be removed before entering the plane. Also, all zip bags used by passengers to pack liquids may not be brought into Tanzania, and if passengers used them during the flight, they must remain on the plane. We ask all travelers to avoid packing or carrying any type of plastic bags to this destination.If you want to rent a vehicle or motorcycle in Zanzibar, you need an international driver\'s license, but also a license that you must get in Zanzibar, at the competent police station, or in Stone Town if you want to drive around the whole island. . We ride local buses.',NULL,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('0d261d05-290a-4f06-bc0a-f63022780219','souvenirs','As for souvenirs, we recommend traditional wooden handicrafts, Islamic ceramics, miniatures, spices, teas, coffee, pistachios, scarves and scarves, as well as figurines and magnets with various Moroccan symbols. The prices of souvenirs are very reasonable, and tipping and haggling are part of the tradition, especially at the stalls in the medina and especially in Fez.',NULL,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('0f43ab6c-4efd-4c4b-af4f-63c184693bb0','other notes','During your tourist stay in this country, you can drive a motor vehicle with a driver\'s license of the Republic of Serbia. To rent a car, you must have a valid passport, driver\'s license and be over 21 years old.',NULL,'28003ef0-871f-4630-a975-885407725ef2'),('1456dfe1-9c62-4c1e-a8ac-a6c194cc72c8','money','The Mexican peso is the official currency in Mexico and its exchange rate is 1€ = 23 pesos, 1$ = 20 pesos. In many places you can pay in US dollars, but it is recommended to carry banknotes printed after 2006. In some places you can also pay by card, and there are numerous ATMs, although it is recommended to carry cash with you.',NULL,'6d9499d0-d70d-4c29-bb0d-5aefb80e77e5'),('156a13b8-8fe4-4b5c-8a09-5d23d80fcc30','food and drinks','The food is very diverse, so to speak typically Asian. There is a lot of rice, fish, noodles, chicken, fruits and vegetables. Thai cuisine is one of the best cuisines in the world and is a product of traditional Eastern, but also increasingly Western culinary influence. The hallmarks of that exotic cuisine are chili peppers, garlic, coriander, Thai basil, lime, mint, lemongrass, galangal, tamarind and imaginative curry - red, green and yellow - mashaman curry, but also a combination of prince, coconut, banana, pineapple, papaya, mango, peanut, meat, squid, shrimp and seafood. The specialty of Thai cuisine is Pad Thai - a dish made of rice noodles, vegetables, meat and enriched with Thai spices. In addition, in Thailand you can try various soups, fried rice with toppings and various exotic combinations of salty and sweet, meat and fruit. If you don\'t eat spicy food, tell the waiter, because chili is very common in Thai food. Street food is, according to many, the tastiest, and there are a large number of restaurants serving local and international cuisine, so you won\'t go hungry. The food is very affordable.You will find fresh fruit and squeezed fruit juices at every step, and at very reasonable prices. For sweets lovers, there is Mango sticky rise (Mango with sweet rice) and Roti - a type of pancake.It is important to note that you must drink bottled water.',NULL,'7172d74b-e2d7-42b7-9b86-1de556740e09'),('163b134f-4ca1-43c4-9307-9744cb106cd8','food','The mixed colonial past has reflected on the culture of Mauritius. The cuisine is a mixture of Indian, French and Creole cuisine, characterized by extremely spicy food with a strong taste. The population usually spends their evenings in one of the large number of restaurants throughout the island, and you can find food for everyone\'s tastes, from Indian restaurants to Chinese, Creole, South African, and restaurants with European cuisine. Large international restaurant chains are also present. Mauritius can also boast of quality beer, as well as rum made from sugar cane, since the time of the first colonists. In the 19th century, the production of rum contributed a lot to the economic boom when numerous distilleries were founded. Bottled drinking water is recommended.',NULL,'bb4e3ee9-8b25-4244-9341-1eff83b3d4a5'),('16406ed7-539e-4789-98e7-709ba14cb0fc','health situation','Water is not potable, only bottled water is used and ice is avoided. Bottled water is also used for brushing teeth. It is recommended that you have health insurance that you can take out at the agency up to 5 days before the trip. For the insurance price, call the agency.',NULL,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('18266744-fa2c-4f00-8136-d5af7aaf2a5a','money','The Thai baht is the official currency of Thailand. The symbol for the baht is ฿, the international symbol is THB. As far as money is concerned, the relationship between the dollar and the euro in Thailand is very similar to ours. There is no need to change money before leaving for the trip. Also, if you have dollars, that\'s fine too, because you\'ll definitely need to exchange money everywhere and pay in local currency. The current exchange rate between the euro and the baht is around 1EUR=36 THB, and the dollar and baht is 1USD=34 THB. The banking system is highly developed, so you will find numerous banks and ATMs at every turn. The commission for using an ATM is around BHT 180-200 (€6), but the exact amount of the commission should be checked with the parent bank. Our recommendation is to bring cash. The use of credit cards is possible, but you must notify your bank in advance, so that you do not have problems with blocking the card. Exchanges are also available at every turn, available throughout the day.',NULL,'7172d74b-e2d7-42b7-9b86-1de556740e09'),('19b0edad-0b4a-4300-a8d7-649c6d54c986','health','You are not legally required to receive vaccinations to enter Morocco, but be sure to consult your doctor. Drinking bottled water is recommended. Of the medicines, bring with you medicines for regular therapy if you have it, probiotics for stomach problems, medicines for reducing fever, painkillers, that is, medicines that you generally take with you on a trip. It is necessary to bring a sun cream with you.',NULL,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('1f4c8464-a598-4532-ab52-fe6136e9baae','safety','Tanzania and Zanzibar are safe destinations, but only if you follow certain rules. Zanzibar is a safe island during the day, especially in touristic locations. At night, it is recommended to move in a group. Locals are extremely friendly towards tourists and love to socialize and meet new people. What\'s more, most locals are ready to help you with anything, without asking for anything in return. Attention should be paid to street vendors who can often be pushy in their desire to sell souvenirs. They are able to tirelessly follow tourists, which can be uncomfortable for someone. In Zanzibar there is a Maasai minority, who mostly keep to themselves and work as security guards at hotels and souvenir shops. Some locals have realized that it is interesting for tourists to dress up as Maasai warriors, and often try to sell illegal substances. Any use of intoxicating substances is prohibited by law and any offers should be avoided. Be careful when taking photos, because if you want to take a picture of someone, you must ask. It is not recommended to tour Dar es Salaam on your own.',NULL,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('2029d729-f4e7-44f7-849f-878100157d5a','visa','Citizens of the Republic of Serbia need a visa to visit and stay in the Kingdom of Thailand. Documentation required for visa: passport (valid for 6 months after intended entry into Thailand),one photo on a white background (dimensions 4cm x 6cm),photocopy of the first page of the passport,a copy of the purchased airline ticket,the completed form that you receive at our agency.The visa is issued a month before the trip, when you receive all the information from the agency that will mediate in obtaining it.',1,'7172d74b-e2d7-42b7-9b86-1de556740e09'),('2a8b1db8-07f5-4a1f-9613-652929acf93a','money','The official currency is the Tanzanian Shilling - TZS. The ratio of the local currency in relation to dollars and euros is 1 € = 2320 TZS, 1 $ = 2180 TZS. It is recommended that you carry dollars with you, but only those printed in 2006 and younger. ATMs exist but are not easily accessible. You can\'t always use the cards. Consult your bank for details and be sure to report going abroad so that your cards are not blocked. In some cases, you can also pay in dollars, but prepare smaller coins and one dollar will cost you about 2000 TZS. Always haggle at markets, souvenir shops and street vendors, as it is customary. Also, Zanzibar is one of those places where it is understood that you have to leave a tip when you are served. If you don\'t, you will be considered uncultured and you will get a lower quality of service next time. The amount of the tip usually depends on the service itself, but it goes something like this:from $5 to $10 per day tip for local guide, $1 for bag porter, 10% of total restaurant order for waiters, $1 per day for housekeepers.',NULL,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('2ebe504b-db90-436b-9a9b-3fcc64bf2e61','safety','Mexico belongs to medium risk countries. In Mexico City, it is recommended not to move in certain areas of the city, outside of the itinerary. The Caribbean region is a safe and secure zone.',NULL,'6d9499d0-d70d-4c29-bb0d-5aefb80e77e5'),('31736d08-3df3-44a0-87cd-60ff5df7d602','PCR test','A negative PCR test, not older than 72 hours, is necessary. Upon arrival, all passengers undergo additional testing (quick test) at their own expense ($25). Before arriving in Tanzania (within 24 hours), all travelers must complete a form on the Tanzania Ministry of Health website.',1,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('36ee512d-d9d4-47d1-ad76-92ebd8690291','health situation','Vaccination is optional. Our passengers decide individually whether they want to be vaccinated or not. Best to call the Institute of Tropical Diseases and check. It is advisable to bring stomach medicine (probiotics), Fervex or some medicine for pain and fever, just in case. If you don\'t bring it, it\'s not terrible, everything can be bought in the pharmacies there. Also, there are mosquitoes there, so it would be good to bring Autan, and you can also get mosquito repellent there, from experience, their repellent is stronger, so you can buy it in Bangkok.',NULL,'7172d74b-e2d7-42b7-9b86-1de556740e09'),('378ce7af-4c02-4173-963b-6ff1b9dac085','safety','The situation in Thailand is generally stable and peaceful. Citizens, if they are visiting Thailand, are advised to be careful. It is recommended to carefully store personal documents and money due to the risk of robbery and pickpocketing. Walking on the street late in the evening is only recommended if you are not alone. Drugs are an illegal phenomenon, and as such punishable by law and imprisonment.',NULL,'7172d74b-e2d7-42b7-9b86-1de556740e09'),('45d4ddf7-902f-4c83-9c64-ae6f31ac8049','souvenirs','To begin with, we must mention that it is forbidden to bring out shells, corals and minerals and other objects from nature. From souvenirs, we recommend: famous paintings of the Tingatinga technique, traditional clothing and materials, wooden objects and sculptures, coffee from Kilimanjaro, traditional music, jewelry, objects related to the Maasai culture, spices from Zanzibar...',NULL,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('47a33f47-fb13-4e28-a5f6-e186d5f46d06','insurance','To enter Cuba, it is necessary to have international health insurance with you. You can get it at any insurance company or at our agency up to 5 days before the trip - UNIQA insurance, you are insured up to €15,000.',1,'28003ef0-871f-4630-a975-885407725ef2'),('4aa18d45-061a-49e4-953f-587beeace584','money','The official currency of the Maldives is the Maldivian Rufiyaa, which is divided into 100 Laari. The code for the digital currency is MVR, local code Rf. Banknotes issued by the Maldives Monetary Authority (MMA) consist of denominations of 1, 5, 10, 25, 50 Laari, 1 Rf and 2 Rf. Payment is also possible in US dollars. It is not recommended to carry banknotes printed before 2006. Also, in most hotels, restaurants and shops you can pay with American Express, Visa International, Master Card, Diners Club and EuroCard payment cards.',NULL,'5d92b93e-82c4-4332-8a14-d158f21ee488'),('4af559d3-b845-43c3-87b8-853e71908939','visa','Citizens of the Republic of Serbia need visas to enter the territory of Tanzania (to which the island of Zanzibar also belongs). A visa is obtained upon entering the country (at the airport) and costs $50. It is not necessary to submit documentation, but only to fill out the form and bring a photo on a white background measuring 3.5 x 4.5. As for photos, sometimes they ask for them when getting a visa, sometimes not, but it\'s better to have them with you just in case. The visa is issued with a validity period of 3 months. When crossing over to Zanzibar (in the Tanzania and Zanzibar tour), passport control is passed at the port and a visa for Zanzibar is obtained, free of charge. All of the above applies to citizens of the Republic of Croatia, Bosnia and Herzegovina, Macedonia, Montenegro, but it is necessary to check the visa regime for Tanzania at the home embassy.',1,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('576720f3-fa6e-4f29-b88b-6b5fa9d152b9','money','Cuba is a country that has 2 currencies - CUC ie. convertible peso and CUP ie. peso or moneta nacional. You will only need CUC on the way and this is the currency you get when you exchange money at the exchange. The exchange rate is 1€ = 1.1 CUC. You can also exchange money into CUP, but you can only use that currency at the market in some smaller local shops, and the ratio is 1 CUC = 29 CUP. Money is exchanged in exchange offices that are state-owned so that the exchange rate is identical everywhere. Take euros with you on the trip, since the commissions on dollars are high. It is recommended to carry cash because card payments are not common, and ATMs are not always in operation and there are not many places. Exchanges are called CADECA and they are not in many places. Queues in exchange offices are long, so always set aside a little more time for that, you may have to wait for half an hour. When changing money, you must have your passport with you! Never change money on the street.',NULL,'28003ef0-871f-4630-a975-885407725ef2'),('5a003f41-def0-46ca-92b2-a249241bc526','safety and security','The cities and places visited on the tour are safe, but we definitely advise you to be careful and considerate when it comes to your personal belongings (as in any European or other city). In the souks as well as in the main square of Djema el Fna in Marrakesh, large crowds are created. Although there is a police station in the main square and a large number of plainclothes police on the ground, petty thefts occasionally occur. Keep all valuables in the hotel safe. It is not recommended for women to walk alone, and in the evening and at night we advise you not to separate from the group. Do not go to parts of the city that the guide notes as unsafe. Avoid consuming alcohol in public places, especially during the religious holiday of Ramadan. Drugs are an illegal phenomenon, and as such punishable by law and imprisonment. Leave your passport, payment cards and other valuables in the room. If you think that your passport is still necessary, always have a copy of it (printed or emailed) with you. Sellers can also be aggressive in wanting you to buy something from them and offer you tea, and then as a sign of hospitality on their part, expect you to buy something in return. Determine the price of the taxi before getting into the vehicle, otherwise it will be many times higher when you arrive at your destination. It is even better to demand that the driver write the number on a piece of paper, because later he will not be able to claim that you did not understand each other well.',NULL,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('5b1c161a-c5f6-4fcc-97ef-ecae81793150','food and drinks','The food in Mexico is very tasty, but also exotic and completely different from the Mexican cuisine we are used to in our restaurants. Mexican food has a reputation for being extremely spicy. True, but we note that the original food is not spicy and hot, but the spiciness is given by various sauces that are added afterwards. We definitely advise you to try Mexican specialties such as tacos, burritos, gorditas, quesadillas with different fillings and types of meat. In Mexico, there are also international restaurants, for all those who are not fans of Mexican cuisine. The most popular drinks are fresh fruit juices, beer, tequila and mezcal. The difference between tequila and mezcal is the type of agave used - tequila is made exclusively from blue agave, and mezcal from all types of agave.',NULL,'6d9499d0-d70d-4c29-bb0d-5aefb80e77e5'),('5e2bf6c5-9f7f-42e0-b445-d07b8d7844df','beaches','You will have the opportunity to swim and sunbathe when you come to the Yucatan and the state of Quintana Roo. Sandy beaches will be near your accommodation. You should know that sunbeds are charged, they often have a fixed price, but you can always haggle and the price is variable from bar to bar, but there are also parts where you don\'t have to rent sunbeds. Keep cameras and mobile phones away from sand, it often happens that the wind blows and fills all your things with fine powdery sand, and the device may malfunction. Also watch out for seagulls, sometimes they want to steal your food... In the last few years, due to global warming, there is a greater amount of seaweed during the summer months, from May to October. The sea is still clean, only algae are unavoidable.',NULL,'6d9499d0-d70d-4c29-bb0d-5aefb80e77e5'),('60c3b97d-d66a-4435-9164-9573d174b9d2','vaccination','Neither vaccine is required to enter Tanzania. If you are coming to Zanzibar by plane, you do not need a yellow card or any vaccinations. Also, it is not necessary to take any medicines. As for anti-malarial drugs, it is not necessary to take them, but consult your doctor about this. It is important to know that medicines do not protect 100% against malaria and can have side effects. Among the other medicines, take with you regular therapy if you have it, probiotics, medicines to lower the temperature, painkillers, that is, medicines that you generally take with you on a trip. Be sure to bring sunscreen and Autan.',NULL,'5a18cc3d-5bb1-47b4-a902-4204c98c6070'),('62bf012b-b158-457e-a1e2-84c5094055f6','money','The official currency is the Indonesian rupiah (IDR). The euro ratio is as follows: 1€ = 114880 IDR. ATMs exist, but cannot be relied upon. You can\'t always use the cards. Consult your bank for details and be sure to report going abroad so that your cards are not blocked.',NULL,'a35cd734-9c8d-4be6-9e1e-400682d2568c'),('6aafd8aa-0a1f-47ff-9f38-9f47c3c09706','recommendation','In the last 10 years, the Kingdom of Thailand has become the promised land for all those who believe in alternative medicine. So you can visit one of the many spas, take a meditation course and teach your mind and body to become relaxed. There is also the famous Thai massage, which has become popular all over the world. You will find massage parlors at every turn and at very reasonable prices.',NULL,'7172d74b-e2d7-42b7-9b86-1de556740e09'),('6ab786be-0063-4e5c-b546-708214d03adf','visa','Citizens of the Republic of Serbia do not need a visa for a stay of up to 90 days.',NULL,'28003ef0-871f-4630-a975-885407725ef2'),('6fc5fb26-5fc1-4a49-80b5-8e4cd28b6bff','food and drinks','The traditional diet includes rice, noodles, chicken, beef (Yogjakarta), pork (Bali), vegetables and fruits, seafood and fish. Dishes can be extremely spicy, so it is advised to check before ordering. Street food is recommended (primarily because this is an area with a tradition of street food, you can also try a large number of international cuisines). Alcohol is quite expensive. Also, in most restaurants where the Muslim population eats, don\'t even ask for alcohol. Try kopi luvak coffee, but also the local alcoholic drink Arak, Bintang beer. Wash the fruit with bottled water or peel it. Of the dishes, you must try nasi kampur, nasi goreng (rice-based), mie goreng (noodle-based), gado gado (salad with boiled potatoes), rendang (beef), babi guling (pork). It is customary to leave a tip in restaurants.',NULL,'a35cd734-9c8d-4be6-9e1e-400682d2568c'),('73010454-f001-4c3d-b506-e5e450c037a7','vaccination','It is not necessary to have a health insurance policy or proof of vaccination to travel to the Maldives, unless you are coming from an area affected by yellow fever (certain areas of Central Africa or South America).',NULL,'5d92b93e-82c4-4332-8a14-d158f21ee488'),('75c98c74-2b69-4fe1-9c80-dccc9ca52ca1','vaccination','Vaccination is not required for travelers traveling to Cuba, but it is advised that travelers check individually with the Institute of Tropical Diseases. Most hotels have 24-hour medical service, specialist doctors and nurses. In larger cities, there are specialist clinics for tourists. Consuming bottled water or using water purification tablets is mandatory, thus avoiding any possibility of tropical diseases. It is recommended to carry a first aid kit, personal medicines, antibiotics, anti-diarrhea medicine, mosquito spray, similar to traveling in other tropical countries. You can find the current situation on the health situation in this country on the website of the World Health Organization. Also, there are mosquitoes there, so it would be a good idea to bring Autan as well as sunscreen. All these preparations must be brought to Cuba because there are no large supermarkets there and it is almost impossible to find them at the destination itself.',NULL,'28003ef0-871f-4630-a975-885407725ef2'),('76955ae1-fe4c-4b16-b176-aea1cd2c2c12','souvenirs','As for souvenirs, we recommend traditional clothes and materials, batik, kopi luwak coffee, Garam sweet cigars with cloves, spices, teas, statues of Hindu deities... It is forbidden to bring out shells, corals and other objects from nature.',NULL,'a35cd734-9c8d-4be6-9e1e-400682d2568c'),('7b6d7e78-a946-4b9e-83db-48cf307a4c5f','covid vaccination','Citizens of Serbia need a complete vaccination of 3 doses to enter Bali, but no more than 6 months have passed since the last booster dose. Citizens who have not been vaccinated cannot currently enter the country.',1,'a35cd734-9c8d-4be6-9e1e-400682d2568c'),('7ceff114-ad6e-4c9e-a90c-8a5642201aec','health_situation','Drinking bottled water is recommended. Of the medicines, bring with you medicines for regular therapy if you have it, probiotics, medicines for reducing fever, painkillers, that is, medicines that you generally take with you on a trip. Be sure to bring sunscreen and Autan.',NULL,'a35cd734-9c8d-4be6-9e1e-400682d2568c'),('7e3ceacd-2fc2-4fbe-8b86-fa933df62b84','visa','For citizens of the Republic of Serbia, a visa is required for visiting and staying in the Kingdom of Morocco and is obtained at the Embassy of Morocco in Belgrade. The visa is done one month before the trip, when you receive all the information from the agency.',1,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('8bcbfa7f-256e-40cc-bfcb-60a9b2cd8417','safety','Indonesia is a safe destination, but you need to be careful when it comes to your personal belongings, especially on the streets, where there are more crowds or in the subway. Pay special attention to things when walking in the evening in Yogyakarta or going out in Bali. Avoid any intoxicants, all opiates are prohibited and illegal, and possession of illegal substances is punishable by death! Be careful when taking photos, because if you want to sneak someone in, you have to ask. Considering that this is a country where the majority of the population is Muslim, take care and respect the rules of behavior and dress. Be sure to take off your shoes in front of temples and mosques. It is forbidden to bring Durian fruit into transport and hotels and you may pay a fine! In everyday life, the right hand is used the most, because the left is considered impure. Do not turn your feet towards other people. Be sure to take care of monkeys, they can be everywhere, they are not aggressive, but they can scratch you even in the game. They also like to steal things from tourists. Avoid eye contact with monkeys..',NULL,'a35cd734-9c8d-4be6-9e1e-400682d2568c'),('8fcd2412-4ded-47f3-928c-03bb8abe0e57','money','The national currency is the Moroccan dirham (MAD or DHS): 1€ = 11 MAD; 1$ = 9 MAD. For spending in Morocco, it is preferable to have the local currency, although in many places you can also pay in euros. In Morocco, the tradition of haggling is cherished, especially when it comes to buying souvenirs and taking a taxi. There is a system of ATMs and payment cards in Morocco, although payment cards do not work in many places, so it is advisable to carry cash with you.',NULL,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('a0fc6b1a-5b87-4e61-b367-1633d9d7a295','visa','Citizens of Serbia require a visa to enter the country. Citizens of Croatia do not need a visa. For citizens of Serbia, the Embassy of Mexico in Belgrade is responsible and personal presence is necessary. The visa is generally valid for 6 months from the date of issue and it is necessary to check this information when making an appointment at the embassy. This information is very important, so that you don\'t end up in a situation where your visa expires before you start your trip, if you arrange your visa much earlier before departure.',1,'6d9499d0-d70d-4c29-bb0d-5aefb80e77e5'),('a5d0a0b6-bcb0-4f21-8810-7a7630faf59f','safety','The Maldives may be at risk of a tsunami. In such situations, after issuing a warning about the danger by the Maldives Government, it is necessary to follow the instructions broadcast by the local media and act in accordance with them.',NULL,'5d92b93e-82c4-4332-8a14-d158f21ee488'),('b62718d9-4e05-4eee-a67a-d018262a77b5','visa','Citizens of Serbia need a visa to enter the country. It is obtained upon arrival at the airport and costs $35. To obtain a visa, it is necessary to have a valid passport, which must be valid for at least 6 months from the moment of entry into the country..',1,'a35cd734-9c8d-4be6-9e1e-400682d2568c'),('b9f0d500-9b8f-410c-ad00-4c00107f7199','vaccination','There is no obligation to vaccinate persons coming to Mauritius except those coming from regions with malaria or yellow fever, according to the regulations of the World Health Organization.',NULL,'bb4e3ee9-8b25-4244-9341-1eff83b3d4a5'),('c4024f9c-a7dd-4267-8a6f-5aff60a1a4de','visa','When landing at the airport in Mauritius, a tourist visa is obtained for 60 days and is free of charge. The validity period of the passport for travel must be 6 months from the date of planned entry. Additionally, there must be two free pages in the passport when entering the country.',NULL,'bb4e3ee9-8b25-4244-9341-1eff83b3d4a5'),('c5151341-f339-4316-a783-c09fda8b6b90','safety','The situation in Cuba is safe and the crime rate is very low. In any case, caution is advised against petty theft and pickpocketing in large cities and tourist areas. Walking on the street is free and without problems even in the evening hours. Drugs are an illegal phenomenon, and as such punishable by law.',NULL,'28003ef0-871f-4630-a975-885407725ef2'),('caf8daf0-2166-4e7f-8020-0893dd2710ed','health card','When entering the plane/ship, passengers must have a filled-in fiche sanitaire (health card), which is also distributed on the plane or ship (special care is taken to write the correct address during the stay in Morocco, as and 2 telephone numbers at which the traveler will be available, if it is necessary to contact him during the first 10 days of his stay in Morocco).',1,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('ccb90e93-cf8b-4734-8bfc-71b8175ded58','insurance','Insurance is not mandatory, but is recommended. You can get it at any insurance company or at our agency up to 5 days before the trip - UNIQA insurance, for price/sum insured/number of days, call the agency.',NULL,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('ce0e34d3-7a39-4445-86cc-c67e28fa6f1f','insurance','Insurance is not mandatory, but is recommended. You can get it at any insurance company or at our agency up to 5 days before the trip - UNIQA insurance, for price/sum insured/number of days, call the agency.',NULL,'7172d74b-e2d7-42b7-9b86-1de556740e09'),('dae252e9-bb53-4737-a056-d22b7700e259','souvenirs','Tequila, various pieces of clothing, shoes and jewelry with Mexican motifs, liquid vanilla, sombreros, Mayan calendar - these are just some of the souvenirs you can buy in Mexico. You can buy the largest selection of souvenirs at the best prices at the stalls in front of Chichen Itza. Don\'t hesitate to haggle with the locals, because that way you respect their haggling culture, and on the other hand, you give yourself a chance to bargain for your favorite memories cheaply.',NULL,'6d9499d0-d70d-4c29-bb0d-5aefb80e77e5'),('e392487b-9d8d-44e5-878b-9e05a8993942','vaccination','No vaccination is required to enter the country. Drinking bottled water is recommended. It is advisable to bring stomach medicine (probiotics) and Fervex or some medicine for pain and fever, just in case. The general sanitary situation is good. Travel health insurance is recommended.',NULL,'6d9499d0-d70d-4c29-bb0d-5aefb80e77e5'),('f4a1c54d-530f-4b88-b380-91e486c95889','other notes','In Mauritius you drive on the left, like in England. From Plaisance International Airport, there are regular flights to all major world cities. Smoking in public places is prohibited, except in specially marked places.',NULL,'bb4e3ee9-8b25-4244-9341-1eff83b3d4a5'),('f721f906-f404-4ff5-81aa-ddd70231a9ba','visa','Citizens of the Republic of Serbia who travel to the Maldives for tourism receive a free visa valid for a period of up to 30 days at the Maldivian airport. The following documentation is required: a valid travel document, a return air ticket, proof of having sufficient financial resources or a confirmation of the paid tourist package. The validity period of the passport for tourist travel must be at least 6 months.',NULL,'5d92b93e-82c4-4332-8a14-d158f21ee488'),('f8902bd5-f372-4b56-b179-c13aa8d814e8','food and drinks','Moroccan cuisine is very diverse and includes dishes from Europe and the Mediterranean, as well as their Berber roots. One of the most popular Moroccan dishes is cous cous and tagine. The traditional diet includes chicken, lamb and beef in many ways, breads, salads, and dishes that are characteristic of the Middle East and the Islamic countries of North Africa. Moroccans use a lot of vegetables in their meals, so their traditional dishes (couscous and tagine) are meat-based, but with a large amount of vegetables. Be sure to try the traditional Moroccan mint tea and coffee. Alcohol is very rare in public use in Morocco and is indeed rare to find anywhere. Only non-alcoholic beer is sold in markets. In Morocco, use only bottled water! Wash the fruit with bottled water or peel it. Food and drink prices are affordable. The average price of a meal is 5-10 euros.',NULL,'4d012c46-9bc3-4181-93d1-03cc7c1e0643'),('fc63e2f4-42e8-4598-852d-1f75837df5bc','food and drinks','Cuban cuisine is primarily based on fish specialties and seafood, but all types of meat are also represented. The side dish that goes with almost every dish is rice, Moros y Cristianos, that is. rice and black beans. The national dish is Ropa Vieja - beef with vegetables. In Cuba, there are many types of fruits and vegetables that do not grow in Europe (guava, pineapple, malanga, yucca...). It is recommended to eat food exclusively from restaurants, except for fruits and vegetables that are available in the markets. The prices are the same as in Europe (roughly a meal between 10-15eur). It is important to note that bottled water must be consumed.',NULL,'28003ef0-871f-4630-a975-885407725ef2');
/*!40000 ALTER TABLE `state_informations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `basic_info` varchar(1000) NOT NULL,
  `world_destination_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `world_destination_id` (`world_destination_id`),
  CONSTRAINT `states_ibfk_1` FOREIGN KEY (`world_destination_id`) REFERENCES `world_destinations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES ('28003ef0-871f-4630-a975-885407725ef2','cuba','Cuba is an island country in Central America. It is also the largest island in the Caribbean, made up of 4,000 smaller islands and archipelagos. It has the shape of an alligator, so it is popular among Latin Americans under the name El Cayman. The capital and largest city is Havana with about 2 million inhabitants, while the entire country has 11 million inhabitants. On the south side, it faces the Caribbean Sea, while on the north, it faces the Gulf of Mexico and the Atlantic Ocean. In Cuba, you will enjoy music, cocktails and beaches with white sand. But in addition, you will have the opportunity to visit the rural parts of Cuba and to get acquainted with the ways of making the famous Cuban cigars. For those who like a little active vacation, you will have the opportunity to hike through the rainforest and swim under the waterfall itself. Cuba has a lot to offer so you\'ll have the chance to both relax and explore!','3799520d-1217-4b8c-b194-ff2f9347faa9'),('4d012c46-9bc3-4181-93d1-03cc7c1e0643','morocco','Morocco, or officially the Kingdom of Morocco, is a North African country with a turbulent history and intense life. It is located in the Maghreb region, facing the Atlantic Ocean in the west and the Mediterranean Sea in the north. The capital is Rabat, and the largest city is the port of Casablanca on the Atlantic Ocean. The living coastline of lush vegetation, the desert, as well as several mountain ranges make up the geographical features of this country. Morocco is a country of beautiful cities, Islamic architecture, luxurious beaches, barbers, camels, friendly people, constant sunshine, full of strong smells, spices and very tasty food. Tourism is Morocco\'s second largest industry, after phosphate sales. Also, Morocco is the world\'s largest producer of argan oil.','f1d550c2-6c64-40d5-981a-852de21e0a78'),('5a18cc3d-5bb1-47b4-a902-4204c98c6070','zanzibar','Known as a tropical paradise, this island, which is part of Tanzania, represents much more than beautiful beaches and magical nature. Actually, Zanzibar is an archipelago consisting of two main islands - Unguja (also called Zanzibar) and Pemba. Let the charm, excellent service and friendliness of Zanzibar locals inspire all your senses and allow you to create memories that will last a lifetime. The aromas of cinnamon, cloves and nutmeg will take you on a journey through the ages - take some time off and go on spice tours and discover some of the greatest secrets of Zanzibar specialties. Explore the narrow streets of Stone Town, shop from the locals and get to know their culture and traditions.','f1d550c2-6c64-40d5-981a-852de21e0a78'),('5d92b93e-82c4-4332-8a14-d158f21ee488','maldives','The Maldives, officially the Republic of Maldives, is an island nation in the Indian Ocean, southwest of the Indian peninsula. They consist of about 1,200 coral islands grouped into 26 atolls, of which about 200 are inhabited, and the other 80 are used for tourism. There are no rivers or lakes in this state, but it is surrounded on all sides by the Indian Ocean. It is recognizable in the world for its long, white sandy beaches, incredible blue water and is a dream destination.','a43de155-6ad8-4afd-b5ab-240db9e89e15'),('6d9499d0-d70d-4c29-bb0d-5aefb80e77e5','mexico','Mexico or, officially, the United Mexican States is located in North America, and is bordered to the north by the United States of America, and to the southeast by Guatemala and Belize. Mexico also borders the Pacific Ocean to the west and the Gulf of Mexico and the Caribbean Sea to the east. The capital and largest city is Mexico City. In pre-Columbian Mexico, there were many Indian cultures that created advanced civilizations such as the Olmecs, Toltecs, Zapotecs, Mayas and Aztecs, whose archaeological sites are of great importance for the culture and history of this country today. Mexico gained independence from Spain in 1821. The first associations we all have with Mexico today are sombreros, tequila, mariachis, tacos, burritos, white sandy beaches, archaeological sites, cenotes. With the Smiling Tribe you will have the opportunity to enjoy all the charms of this Caribbean country, swim with dolphins, swim in natural pools - cenotes, drink tequila on the beautiful beaches of Cancun','3799520d-1217-4b8c-b194-ff2f9347faa9'),('7172d74b-e2d7-42b7-9b86-1de556740e09','thailand','Thailand, officially the Kingdom of Thailand, is a country in Southeast Asia; in the southwest it opens to the Andaman Sea (part of the Indian Ocean), and in the southeast to the Gulf of Thailand (part of the South China Sea). It borders Myanmar (Burma) to the west, Laos to the north and east, Cambodia to the east and Malaysia to the south. Thailand is a land of islands, exotic beaches, crystal seas, nightlife, Buddhism, magic and adventure. A real treasure trove of interesting stories woven from culture and philosophy, incredible landscapes and beautiful beaches. Although many consider Thailand an island, it is actually a mainland country that has access to the Andaman Sea and the Gulf of Thailand, but it has over 1400 islands, the most famous of which are Phuket, Koh Pangan, Krabi and Ko Samui. The smile and hospitality of the Thai people awaits you at every corner. Swimming, massages, white sand, turquoise, warm sea, phenomenal sunsets and trips to nearby islands will make you feel ','a43de155-6ad8-4afd-b5ab-240db9e89e15'),('a35cd734-9c8d-4be6-9e1e-400682d2568c','bali','The Republic of Indonesia is a country in Southeast Asia. It comprises an archipelago of 13,466 islands and is the largest island nation in the world in terms of both population and area. The most populated islands are Java and Sumatra, and the most famous and most visited by tourists is Bali. Bali is a popular tourist destination, the local population lives and works from tourism, in addition to agriculture, there are a large number of hotels and resorts in Bali, because the island is visited by millions of tourists every year. The island is rich in fish, rice, coconut palms, bananas, pineapples, cocoa, coffee, cotton and tobacco, so these are the goods it exports the most.','a43de155-6ad8-4afd-b5ab-240db9e89e15'),('bb4e3ee9-8b25-4244-9341-1eff83b3d4a5','mauritius','Mauritius is an island country in the western part of the Indian Ocean. This small island, which was discovered by the Portuguese in 1505, attracts an increasing number of visitors from all over the world every year, and is especially popular among nature lovers, divers and all those who want to relax on beautiful white beaches and swim in the turquoise ocean. It is completely surrounded by a coral reef, which is why it is characterized by an extraordinary richness of the underwater world. Mauritius is known for its rich history influenced by three great cultures - French, British and Asian. Mauritius is officially treated as one of the most developed countries on the African continent. In addition to income from tourism, this island is also known as a significant producer and exporter of sugar. The sugarcane plantations are really huge and spread over the entire surface of the island.','f1d550c2-6c64-40d5-981a-852de21e0a78');
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travelers`
--

DROP TABLE IF EXISTS `travelers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `travelers` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `telephone_number` varchar(50) NOT NULL,
  `passport_number` varchar(20) NOT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `passport_number` (`passport_number`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `travelers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travelers`
--

LOCK TABLES `travelers` WRITE;
/*!40000 ALTER TABLE `travelers` DISABLE KEYS */;
INSERT INTO `travelers` VALUES ('1b01cbde-4e12-4d2e-adff-c70e28cd0f2a','Emilija','Milenkovic','0631528496','11111','828eb26d-1b70-4604-bfbc-86b09400dbd3'),('4f2b8e35-05a0-477e-a344-94cd725dd717','Pera','Peric','0695812365','22222','7cb7de93-fa44-461e-b68b-bca24f49c65c'),('5d3e8046-255a-45c1-93cc-06ea4ce4d1ac','Ana','Anic','0652314879','44444','4036fa9b-d7ae-44ea-bf33-6876f1eaeca5'),('661f2223-c114-42db-a31b-50bc56b5c10d','Mara','Maric','0632518496','55555','06ecb681-3ef9-4d2d-924e-236c19b5e93f'),('b53ba486-057f-4cc9-a799-97dd43048614','Mika','Mikic','0625148795','33333','d2b8effe-c727-420f-bc39-320a2eaf206c');
/*!40000 ALTER TABLE `travelers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travelers_booked_arrangements`
--

DROP TABLE IF EXISTS `travelers_booked_arrangements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `travelers_booked_arrangements` (
  `id` varchar(50) NOT NULL,
  `arrangement_id` varchar(50) DEFAULT NULL,
  `traveler_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `arrangement_id` (`arrangement_id`),
  KEY `traveler_id` (`traveler_id`),
  CONSTRAINT `travelers_booked_arrangements_ibfk_1` FOREIGN KEY (`arrangement_id`) REFERENCES `arrangements` (`id`),
  CONSTRAINT `travelers_booked_arrangements_ibfk_2` FOREIGN KEY (`traveler_id`) REFERENCES `travelers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travelers_booked_arrangements`
--

LOCK TABLES `travelers_booked_arrangements` WRITE;
/*!40000 ALTER TABLE `travelers_booked_arrangements` DISABLE KEYS */;
/*!40000 ALTER TABLE `travelers_booked_arrangements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travelers_mandatory_checks`
--

DROP TABLE IF EXISTS `travelers_mandatory_checks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `travelers_mandatory_checks` (
  `id` varchar(50) NOT NULL,
  `is_fulfilled` tinyint(1) NOT NULL,
  `booked_arrangement_id` varchar(50) DEFAULT NULL,
  `state_info_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `check_uc` (`booked_arrangement_id`,`state_info_id`),
  KEY `state_info_id` (`state_info_id`),
  CONSTRAINT `travelers_mandatory_checks_ibfk_1` FOREIGN KEY (`booked_arrangement_id`) REFERENCES `travelers_booked_arrangements` (`id`),
  CONSTRAINT `travelers_mandatory_checks_ibfk_2` FOREIGN KEY (`state_info_id`) REFERENCES `state_informations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travelers_mandatory_checks`
--

LOCK TABLES `travelers_mandatory_checks` WRITE;
/*!40000 ALTER TABLE `travelers_mandatory_checks` DISABLE KEYS */;
/*!40000 ALTER TABLE `travelers_mandatory_checks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travelers_wish_list`
--

DROP TABLE IF EXISTS `travelers_wish_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `travelers_wish_list` (
  `arrangement_id` varchar(50) NOT NULL,
  `traveler_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`arrangement_id`),
  KEY `traveler_id` (`traveler_id`),
  CONSTRAINT `travelers_wish_list_ibfk_1` FOREIGN KEY (`arrangement_id`) REFERENCES `arrangements` (`id`),
  CONSTRAINT `travelers_wish_list_ibfk_2` FOREIGN KEY (`traveler_id`) REFERENCES `travelers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travelers_wish_list`
--

LOCK TABLES `travelers_wish_list` WRITE;
/*!40000 ALTER TABLE `travelers_wish_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `travelers_wish_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('06ecb681-3ef9-4d2d-924e-236c19b5e93f','user5@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',0),('4036fa9b-d7ae-44ea-bf33-6876f1eaeca5','user4@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',0),('51d04d09-6fc7-44ba-b645-baaf074ed0b0','itbootcamp.travel@gmail.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',1),('7cb7de93-fa44-461e-b68b-bca24f49c65c','user2@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',0),('828eb26d-1b70-4604-bfbc-86b09400dbd3','user1@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',0),('d2b8effe-c727-420f-bc39-320a2eaf206c','user3@example.com','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `world_destinations`
--

DROP TABLE IF EXISTS `world_destinations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `world_destinations` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `world_destinations`
--

LOCK TABLES `world_destinations` WRITE;
/*!40000 ALTER TABLE `world_destinations` DISABLE KEYS */;
INSERT INTO `world_destinations` VALUES ('f1d550c2-6c64-40d5-981a-852de21e0a78','africa'),('a43de155-6ad8-4afd-b5ab-240db9e89e15','asia'),('3799520d-1217-4b8c-b194-ff2f9347faa9','central america');
/*!40000 ALTER TABLE `world_destinations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 17:02:58
