import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel18FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel18FlatComponentChunk36

end RHP2Bridge
