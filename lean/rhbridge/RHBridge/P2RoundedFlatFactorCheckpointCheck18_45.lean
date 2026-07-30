import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel18FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel18FlatComponentChunk45

end RHP2Bridge
