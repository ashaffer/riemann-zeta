import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel29FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel29FlatComponentChunk31

end RHP2Bridge
