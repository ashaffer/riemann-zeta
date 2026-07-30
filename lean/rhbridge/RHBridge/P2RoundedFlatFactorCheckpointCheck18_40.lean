import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel18FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel18FlatComponentChunk40

end RHP2Bridge
