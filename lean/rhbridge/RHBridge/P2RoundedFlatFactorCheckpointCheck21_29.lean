import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel21FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel21FlatComponentChunk29

end RHP2Bridge
