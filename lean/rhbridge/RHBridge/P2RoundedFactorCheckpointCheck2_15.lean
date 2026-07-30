import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk15 :
    P2RoundedFactorCheckpointData.panel2Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix60_eq :
    P2RoundedFactorCheckpointData.panel2Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk15.1

theorem panel2Prefix61_eq :
    P2RoundedFactorCheckpointData.panel2Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk15.2.1

theorem panel2Prefix62_eq :
    P2RoundedFactorCheckpointData.panel2Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk15.2.2.1

theorem panel2Prefix63_eq :
    P2RoundedFactorCheckpointData.panel2Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk15.2.2.2

end RHP2Bridge
