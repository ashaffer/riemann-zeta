import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel29FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel29FlatComponentChunk30

end RHP2Bridge
