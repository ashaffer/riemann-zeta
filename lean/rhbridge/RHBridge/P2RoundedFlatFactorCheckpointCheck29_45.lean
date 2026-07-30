import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel29FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel29FlatComponentChunk45

end RHP2Bridge
