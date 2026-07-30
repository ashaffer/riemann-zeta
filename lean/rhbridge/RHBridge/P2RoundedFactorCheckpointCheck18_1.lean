import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk1 :
    P2RoundedFactorCheckpointData.panel18Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix4_eq :
    P2RoundedFactorCheckpointData.panel18Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk1.1

theorem panel18Prefix5_eq :
    P2RoundedFactorCheckpointData.panel18Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk1.2.1

theorem panel18Prefix6_eq :
    P2RoundedFactorCheckpointData.panel18Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk1.2.2.1

theorem panel18Prefix7_eq :
    P2RoundedFactorCheckpointData.panel18Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk1.2.2.2

end RHP2Bridge
