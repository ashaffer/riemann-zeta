import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk8 :
    P2RoundedFactorCheckpointData.panel16Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix32_eq :
    P2RoundedFactorCheckpointData.panel16Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk8.1

theorem panel16Prefix33_eq :
    P2RoundedFactorCheckpointData.panel16Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk8.2.1

theorem panel16Prefix34_eq :
    P2RoundedFactorCheckpointData.panel16Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk8.2.2.1

theorem panel16Prefix35_eq :
    P2RoundedFactorCheckpointData.panel16Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk8.2.2.2

end RHP2Bridge
