import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk15 :
    P2RoundedFactorCheckpointData.panel13Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix60_eq :
    P2RoundedFactorCheckpointData.panel13Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk15.1

theorem panel13Prefix61_eq :
    P2RoundedFactorCheckpointData.panel13Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk15.2.1

theorem panel13Prefix62_eq :
    P2RoundedFactorCheckpointData.panel13Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk15.2.2.1

theorem panel13Prefix63_eq :
    P2RoundedFactorCheckpointData.panel13Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk15.2.2.2

end RHP2Bridge
