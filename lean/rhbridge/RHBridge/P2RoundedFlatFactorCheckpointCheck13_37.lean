import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel13FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel13FlatComponentChunk37

end RHP2Bridge
