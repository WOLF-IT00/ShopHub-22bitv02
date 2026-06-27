import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import productApi from "../api/productApi";


const ProductDetail = () => {

  const { id } = useParams();

  const [product, setProduct] = useState(null);


  useEffect(() => {

    productApi.getById(id)
      .then((response) => {

        setProduct(response.data);

      })
      .catch((error) => {

        console.log("Lỗi lấy chi tiết sản phẩm:", error);

      });

  }, [id]);



  if (!product) {

    return (
      <h2>
        Loading...
      </h2>
    );

  }



  return (

    <div>

      <h1>
        Product Detail
      </h1>


      <h2>
        {product.name}
      </h2>


      <p>
        Price: {product.price} VND
      </p>


      <p>
        Category: {product.category}
      </p>


      <p>
        Description: {product.description}
      </p>


    </div>

  );

};


export default ProductDetail;

