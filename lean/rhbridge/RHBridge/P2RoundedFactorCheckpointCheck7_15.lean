import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk15 :
    P2RoundedFactorCheckpointData.panel7Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix60_eq :
    P2RoundedFactorCheckpointData.panel7Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk15.1

theorem panel7Prefix61_eq :
    P2RoundedFactorCheckpointData.panel7Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk15.2.1

theorem panel7Prefix62_eq :
    P2RoundedFactorCheckpointData.panel7Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk15.2.2.1

theorem panel7Prefix63_eq :
    P2RoundedFactorCheckpointData.panel7Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk15.2.2.2

end RHP2Bridge
