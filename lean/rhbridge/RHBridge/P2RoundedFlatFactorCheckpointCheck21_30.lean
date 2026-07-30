import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel21FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel21FlatComponentChunk30

end RHP2Bridge
