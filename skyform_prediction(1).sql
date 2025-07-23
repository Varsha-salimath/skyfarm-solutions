-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 22, 2024 at 02:51 PM
-- Server version: 5.7.23-23
-- PHP Version: 8.1.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nexgaw7q_internship_projects`
--

-- --------------------------------------------------------

--
-- Table structure for table `skyform_prediction`
--

CREATE TABLE `skyform_prediction` (
  `id` int(100) NOT NULL,
  `area_size` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `plant_type` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `soil_type` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `window_exposure` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `water_frequency` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `climate_zone` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `light_intensity` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `plant_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `plant_description` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `skyform_prediction`
--

INSERT INTO `skyform_prediction` (`id`, `area_size`, `plant_type`, `soil_type`, `window_exposure`, `water_frequency`, `climate_zone`, `light_intensity`, `plant_name`, `plant_description`) VALUES
(1, 'Small', 'Vegetable', 'Loamy', 'North-facing', 'Weekly', 'Temperate', 'Medium', 'Lettuce', 'A leafy vegetable often used in salads'),
(2, 'Medium', 'Vegetable', 'Sandy', 'East-facing', 'Twice a week', 'Temperate', 'Medium', 'Carrot', 'A root vegetable with an orange color, commonly eaten raw or cooked'),
(3, 'Large', 'Vegetable', 'Clay', 'South-facing', 'Weekly', 'Tropical', 'High', 'Cabbage', 'A leafy green vegetable commonly used in soups and salads'),
(4, 'Small', 'Vegetable', 'Loamy', 'West-facing', 'Twice a week', 'Arid', 'Low', 'Spinach', 'A leafy green vegetable rich in iron and vitamins'),
(5, 'Medium', 'Vegetable', 'Silty', 'South-facing', 'Weekly', 'Tropical', 'High', 'Tomato', 'A red, round fruit often used in salads and sauces'),
(6, 'Large', 'Vegetable', 'Loamy', 'North-facing', 'Weekly', 'Temperate', 'Medium', 'Peas', 'Small green legumes that grow in pods and are often eaten in soups or as a side dish'),
(7, 'Small', 'Fruit', 'Sandy', 'East-facing', 'Twice a week', 'Subtropical', 'High', 'Apple', 'A popular round fruit that comes in many varieties, known for its sweet and tart flavors'),
(8, 'Medium', 'Fruit', 'Clay', 'South-facing', 'Weekly', 'Tropical', 'High', 'Banana', 'A long, curved fruit that is yellow when ripe, known for being a quick energy snack'),
(9, 'Large', 'Fruit', 'Loamy', 'West-facing', 'Twice a week', 'Subtropical', 'Medium', 'Orange', 'A citrus fruit known for its refreshing taste and high vitamin C content'),
(10, 'Medium', 'Fruit', 'Silty', 'North-facing', 'Weekly', 'Temperate', 'Low', 'Grapes', 'Small, round, and typically purple or green fruits that grow in clusters'),
(11, 'Small', 'Flower', 'Loamy', 'South-facing', 'Weekly', 'Tropical', 'High', 'Rose', 'A fragrant flower known for its colorful petals and romantic symbolism'),
(12, 'Medium', 'Flower', 'Sandy', 'East-facing', 'Twice a week', 'Temperate', 'Medium', 'Tulip', 'A vibrant, cup-shaped flower, often seen in spring gardens'),
(13, 'Large', 'Flower', 'Clay', 'West-facing', 'Weekly', 'Arid', 'Low', 'Sunflower', 'A tall flower known for its large yellow petals and ability to turn towards the sun'),
(14, 'Medium', 'Flower', 'Silty', 'South-facing', 'Twice a week', 'Tropical', 'High', 'Daffodil', 'A trumpet-shaped flower that blooms in early spring'),
(15, 'Small', 'Flower', 'Loamy', 'East-facing', 'Weekly', 'Temperate', 'Medium', 'Violet', 'A small flower with purple or blue petals, often seen in gardens'),
(16, 'Medium', 'Flower', 'Sandy', 'West-facing', 'Twice a week', 'Subtropical', 'High', 'Chrysanthemum', 'A flowering plant known for its bright colors and ornamental value'),
(17, 'Large', 'Flower', 'Clay', 'North-facing', 'Weekly', 'Tropical', 'High', 'Hibiscus', 'A tropical flowering plant with large, colorful blooms'),
(18, 'Small', 'Other', 'Loamy', 'South-facing', 'Twice a week', 'Temperate', 'Medium', 'Bamboo', 'A fast-growing grass known for its tall, woody stalks'),
(19, 'Medium', 'Other', 'Silty', 'East-facing', 'Weekly', 'Tropical', 'High', 'Palm', 'A tree with large, fan-like leaves that grows in tropical climates'),
(20, 'Large', 'Other', 'Loamy', 'West-facing', 'Weekly', 'Arid', 'Low', 'Cactus', 'A succulent plant with spines instead of leaves, typically found in deserts'),
(21, 'Medium', 'Vegetable', 'Loamy', 'North-facing', 'Weekly', 'Subtropical', 'Medium', 'Onion', 'A vegetable with a strong taste, used in cooking and often eaten raw'),
(22, 'Small', 'Vegetable', 'Clay', 'South-facing', 'Twice a week', 'Arid', 'Low', 'Garlic', 'A bulbous vegetable used to add flavor to a wide variety of dishes'),
(23, 'Large', 'Vegetable', 'Sandy', 'West-facing', 'Weekly', 'Tropical', 'Medium', 'Sweet Potato', 'A starchy root vegetable, often orange or purple in color'),
(24, 'Small', 'Fruit', 'Loamy', 'East-facing', 'Twice a week', 'Subtropical', 'Medium', 'Pineapple', 'A tropical fruit with spiky skin and sweet, juicy flesh'),
(25, 'Medium', 'Fruit', 'Silty', 'West-facing', 'Weekly', 'Tropical', 'High', 'Mango', 'A tropical fruit with a sweet flavor and a large pit in the center'),
(26, 'Large', 'Flower', 'Sandy', 'North-facing', 'Weekly', 'Subtropical', 'Medium', 'Lilies', 'A fragrant flower that blooms in various colors, often used in bouquets'),
(27, 'Medium', 'Other', 'Loamy', 'South-facing', 'Twice a week', 'Arid', 'Low', 'Aloe Vera', 'A succulent plant used for its healing properties, particularly in skin care'),
(28, 'Small', 'Other', 'Silty', 'East-facing', 'Weekly', 'Tropical', 'High', 'Lavender', 'A fragrant herb known for its relaxing scent and purple flowers'),
(29, 'Large', 'Vegetable', 'Clay', 'West-facing', 'Monthly', 'Tropical', 'High', 'Squash', 'A type of gourd with a variety of shapes and sizes, commonly eaten cooked'),
(30, 'Small', 'Fruit', 'Loamy', 'South-facing', 'Weekly', 'Temperate', 'Medium', 'Strawberry', 'A small red fruit that is sweet and juicy, commonly used in desserts');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `skyform_prediction`
--
ALTER TABLE `skyform_prediction`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `skyform_prediction`
--
ALTER TABLE `skyform_prediction`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
