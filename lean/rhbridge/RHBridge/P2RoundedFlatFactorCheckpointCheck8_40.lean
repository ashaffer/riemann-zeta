import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel8FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel8FlatComponentChunk40

end RHP2Bridge
