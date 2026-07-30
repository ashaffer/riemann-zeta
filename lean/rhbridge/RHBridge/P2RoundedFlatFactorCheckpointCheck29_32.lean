import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel29FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel29FlatComponentChunk32

end RHP2Bridge
