import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel13FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel13FlatComponentChunk33

end RHP2Bridge
