import styled from 'styled-components';

const FeaturedProducts = styled.section`
  padding: 40px;
  text-align: center;
`;

const ProductGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 20px;
`;

const ProductCard = ({ product }) => {
    const Card = styled.div`
      border: 1px solid #ddd;
      padding: 20px;
      border-radius: 10px;
      text-align: center;
    `;
    const Image = styled.img`
      width: 100%;
      border-radius: 10px;
    `;
    return (
      <Card>
        <Image src={product.img} alt={product.name} />
        <h3>{product.name}</h3>
      </Card>
    );
  };

const ProductList = () => {
    const products = [
      { id: 1, name: "Stylish Shoes", img: "https://redtape.com/cdn/shop/files/RSO4102_1_c0a68240-77e5-4003-8465-bff2bb2280a7.jpg?v=1738392818" },
      { id: 2, name: "Trendy Bag", img: "https://image.made-in-china.com/202f0j00BeMUEzYJZvbq/Stylish-Cloud-Women-Shoulder-Bags-PU-Leather-Shoulderbag-Women-Handbag-Fashion.jpg" },
      { id: 3, name: "Fashion Sunglasses", img: "https://shoponcliq.com/cdn/shop/products/Vintage-Luxury-Sunglasses-Square-Retro-Fashion-Sunglasses-For-Women-ShopOnCliQ-1488.jpg?v=1722091299&width=1445" },
      { id: 4, name: "Elegant Watch", img: "https://image.made-in-china.com/2f0j00BdzkrVqaJEcU/Poedagar-312-Elegant-Luxury-Watch-for-Women-Stainless-Steel-Band-Quartz-Watches.webp" },
    ];
    return (
      <FeaturedProducts>
        <h2>Featured Products</h2>
        <ProductGrid>
          {products.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </ProductGrid>
      </FeaturedProducts>
    );
  };
  
export default ProductList;  