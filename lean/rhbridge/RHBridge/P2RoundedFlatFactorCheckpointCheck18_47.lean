import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel18FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel18FlatComponentChunk47

end RHP2Bridge
