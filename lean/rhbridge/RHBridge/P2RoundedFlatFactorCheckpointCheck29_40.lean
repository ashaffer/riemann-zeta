import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel29FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel29FlatComponentChunk40

end RHP2Bridge
