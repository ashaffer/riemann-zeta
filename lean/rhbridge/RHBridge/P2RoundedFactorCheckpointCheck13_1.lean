import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk1 :
    P2RoundedFactorCheckpointData.panel13Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix4_eq :
    P2RoundedFactorCheckpointData.panel13Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk1.1

theorem panel13Prefix5_eq :
    P2RoundedFactorCheckpointData.panel13Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk1.2.1

theorem panel13Prefix6_eq :
    P2RoundedFactorCheckpointData.panel13Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk1.2.2.1

theorem panel13Prefix7_eq :
    P2RoundedFactorCheckpointData.panel13Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk1.2.2.2

end RHP2Bridge
