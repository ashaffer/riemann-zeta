import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel12FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel12FlatComponentChunk40

end RHP2Bridge
