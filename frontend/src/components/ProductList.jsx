
import { useEffect, useState } from "react";
import ProductCard from "./ProductCard";
import productApi from "../api/productApi";

const ProductList = () => {
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [sort, setSort] = useState("");

  const [productsData, setProductsData] = useState([]);


  // Gọi API lấy danh sách sản phẩm
  useEffect(() => {

    productApi.getAll()
      .then((response) => {

        setProductsData(response.data);

      })
      .catch((error) => {

        console.log("Lỗi lấy sản phẩm:", error);

      });

  }, []);


  // Lọc sản phẩm
  let filteredProducts = productsData.filter((product) => {

    const matchName = product.name
      .toLowerCase()
      .includes(search.toLowerCase());


    const matchCategory =
      category === "All" ||
      product.category === category;


    return matchName && matchCategory;

  });


  // Sắp xếp giá tăng dần
  if (sort === "asc") {

    filteredProducts.sort(
      (a, b) => a.price - b.price
    );

  }


  // Sắp xếp giá giảm dần
  if (sort === "desc") {

    filteredProducts.sort(
      (a, b) => b.price - a.price
    );

  }


  return (
    <div>

      <h2>Product Catalog</h2>


      <input
        type="text"
        placeholder="Search product..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />


      <br />
      <br />


      <select
        value={category}
        onChange={(e) =>
          setCategory(e.target.value)
        }
      >

        <option value="All">
          All
        </option>

        <option value="Phone">
          Phone
        </option>

        <option value="Laptop">
          Laptop
        </option>

      </select>


      <br />
      <br />


      <select
        value={sort}
        onChange={(e) =>
          setSort(e.target.value)
        }
      >

        <option value="">
          Default
        </option>

        <option value="asc">
          Price Low → High
        </option>

        <option value="desc">
          Price High → Low
        </option>

      </select>


      <hr />


      {
        filteredProducts.map((product) => (

          <ProductCard
            key={product.id}
            product={product}
          />

        ))
      }


    </div>
  );
};


export default ProductList;

