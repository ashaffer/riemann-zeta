import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel18FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel18FlatComponentChunk31

end RHP2Bridge
